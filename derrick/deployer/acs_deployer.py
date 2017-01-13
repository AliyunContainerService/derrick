from aliyunsdkcore.client import AcsClient
from aliyunsdkcs.request.v20151215 import DescribeClustersRequest, DescribeClusterCertsRequest, \
    DescribeClusterDetailRequest
import simplejson as json
import requests
import time
import os
import chalk as log
from derrick.conf.derrick_conf import ScaffoldConf
from derrick.buildpacks.exception import NotFoundAccessKeyInfoInConf

DEFAULT_REGION_ENDPOINT = "cn-hangzhou"


class AcsDeployer():
    def __init__(self):
        sf = ScaffoldConf()
        scaffold_conf = sf.get_scaffold_conf()
        accessKeyId = scaffold_conf.get("AccessKeyId")
        accessKeySecret = scaffold_conf.get("AccessKeySecret")
        if accessKeyId == None or accessKeySecret == None:
            raise NotFoundAccessKeyInfoInConf
        self.sf = sf
        self.cc = ClusterController(accessKeyId, accessKeySecret)

    def get_cluster_list(self):
        cluster_list = self.cc.get_cluster_list()
        clusters = []
        for cluster in cluster_list:
            clusters.append(cluster.get('cluster_id'))
        return clusters

    def deploy_application(self, applicationConf):
        log.green("Start to deploy application")
        cluster_id = applicationConf.get("cluster_id")
        application_name = applicationConf.get("application_name")

        cert_info = self.cc.get_cluster_cert_by_id(cluster_id)
        self.sf.update_cluster_cert(cluster_id, cert_info)

        cluster_info = self.cc.get_cluster_info_by_id(cluster_id)
        master_url = cluster_info.get('master_url')
        cert_path = self.sf.get_cluster_cert_path(cluster_id)
        cwd = os.getcwd()

        cert_path = (
            cert_path + '/cert.pem',
            cert_path + '/key.pem',
        )

        with open(os.path.join(cwd, 'docker-compose.yml')) as f:
            template = f.read()
        f.close()

        req_body = {
            "name": application_name,
            "description": "derrick auto deploy application",
            "template": template,
            "version": str(time.time())
        }
        req_body_str = json.dumps(req_body)
        try:
            response = requests.get(master_url + ('/projects/%s' % application_name), verify=False, cert=cert_path)
            if response.ok:
                pass
            else:
                raise Exception("NotFoundSpecificApplication")

            update_project_url = master_url + ('/projects/%s/update' % application_name)
            response = requests.post(update_project_url, req_body_str, verify=False, cert=cert_path)
        except Exception, e:
            create_project_url = master_url + '/projects/'
            response = requests.post(create_project_url, req_body_str, verify=False, cert=cert_path)

        if response.ok:
            log.green("Deploy application to Aliyun Container Service successfullly!")
        else:
            log.red("Failed to deploy application,because of %s" % response.text)






class ClusterController:
    def __init__(self, AccessKeyId, AccessKeySecret):
        self.access_key_id = AccessKeyId
        self.access_key_secret = AccessKeySecret

        self.client = AcsClient(self.access_key_id, self.access_key_secret, DEFAULT_REGION_ENDPOINT)

    def get_cluster_list(self):
        req = DescribeClustersRequest.DescribeClustersRequest()
        status, header, resp = self.client.get_response(req)
        if status == 200:
            cluster_list = json.loads(resp)
            return cluster_list
        else:
            return None

    def get_cluster_cert_by_id(self, cluster_id):
        req = DescribeClusterCertsRequest.DescribeClusterCertsRequest()
        req.set_ClusterId(cluster_id)
        status, header, res = self.client.get_response(req)
        if status == 200:
            cert_info = json.loads(res)
            return cert_info
        else:
            return None

    def get_cluster_info_by_id(self, cluster_id):
        req = DescribeClusterDetailRequest.DescribeClusterDetailRequest()
        req.set_ClusterId(cluster_id)
        status, header, res = self.client.get_response(req)
        if status == 200:
            cluster_info = json.loads(res)
            return cluster_info
        else:
            return None
