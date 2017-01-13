from derrick.deployer.acs_deployer import AcsDeployer
from derrick.conf.application_conf import ApplicationConf
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

    try:
        # publish latest image to hub
        local.publish(options=None)
        deployer.deploy_application(application_conf)
    except Exception, e:
        log.red("Failed to deploy application to aliyun container service,because of %s" % e.message)
