import simplejson as json
import os
import conf
import chalk as log
import derrick.utils.file as fileUtil

DERRICK_BASE_PATH = os.path.join(os.path.expanduser("~"), ".derrick")
DERRICK_CONF_PATH = os.path.join(DERRICK_BASE_PATH, "derrick.json")


class ScaffoldConf(conf.Configuration):
    path = DERRICK_CONF_PATH

    def get_cluster_cert_path(self, cluster_id):
        return os.path.join(DERRICK_BASE_PATH, cluster_id, "certs")

    def get_buildpack_path(self):
        return os.path.join(DERRICK_BASE_PATH, "buildpacks")

    def update_cluster_certs(self, cluster_id, cert_info):
        ca = cert_info.get('ca')
        cert = cert_info.get('cert')
        key = cert_info.get('key')

        dir_path = self.get_cluster_cert_path(cluster_id)
        if os.path.exists(dir_path) == True:
            pass
        else:
            os.mkdir(dir_path)

        try:
            ca_file = open(os.path.join(dir_path, "ca.pem"), "wa")
            key_file = open(os.path.join(dir_path, "key.pem"), "wa")
            cert_file = open(os.path.join(dir_path, "cert.pem"), "wa")

            ca_file.write(ca)
            ca_file.close()

            key_file.write(key)
            key_file.close()

            cert_file.write(cert)
            cert_file.close()
        except Exception, e:
            log.red("Failed to write cert to derrick path,because of %s" % e.message)

    def get_scaffold_conf(self):
        self.detect_config_path()
        return self.Load()

    @staticmethod
    def init_scaffold_conf(conf):
        try:
            ok = fileUtil.exists(DERRICK_BASE_PATH)
            if ok == False:
                log.red("Failed to create config file in %s" % DERRICK_CONF_PATH)
                exit(-1)
            file = open(ScaffoldConf.path, "w")
            json.dump(conf, file, indent=4)
            return conf
        except Exception, e:
            log.red("Failed to init scaffold conf, because of %s" % e.message)
            exit(-1)
