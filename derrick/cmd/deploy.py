from derrick.deployer.acs_deployer import AcsDeployer
from derrick.conf.application_conf import ApplicationConf
from derrick.conf.derrick_conf import ScaffoldConf
from derrick.buildpacks.exception import NotFoundAccessKeyInfoInConf
import inquirer
import local
import chalk as log


def deploy():
    deployer = AcsDeployer()
    cluster_list = deployer.get_cluster_list()
    ques = [
        inquirer.List('cluster_id',
                      message="Deploy application to a specific cluster",
                      choices=cluster_list,
                      ),
    ]
    answer = inquirer.prompt(ques)
    ApplicationConf.update_application_conf(answer)
    # Reload application conf
    application_conf = ApplicationConf.parse_application_conf()
    if application_conf.get("application_name"):
        ques = [
            inquirer.Text('application_name', message="Please input application name to deploy"),
        ]
        answers = inquirer.prompt(ques)
        ApplicationConf.update_application_conf(answers)
        application_conf = ApplicationConf.parse_application_conf()
    local.publish()
    try:
        # publish latest image to hub
        deployer.deploy_application(application_conf)
    except NotFoundAccessKeyInfoInConf:
        ques = [
            inquirer.Text('AccessKeyId', message="Please input your AccessKeyId"),
            inquirer.Text('AccessKeySecret', message="Please input your AccessKeySecret"),
        ]
        answers = inquirer.prompt(ques)
        sf = ScaffoldConf()
        sf.init_scaffold_conf(answers)
        deployer.deploy_application(application_conf)
    except Exception, e:
        log.red("Failed to deploy application to aliyun container service,because of %s" % e.message)
