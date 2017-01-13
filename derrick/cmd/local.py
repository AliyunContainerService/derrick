from derrick.conf.application_conf import ApplicationConf
import os
import chalk as log


def test():
    cwd = os.getcwd()
    test_image_path = os.path.join(cwd, "Dockerfile.test")
    if os.path.exists(test_image_path) == False:
        log.red("Failed to find Dockerfile.test in path")
        exit(-1)

    application_conf = ApplicationConf.parse_application_conf()
    test_image_repo = application_conf.get("test_image_name")
    cwd = os.getcwd()

    try:
        os.system("docker build -t %s -f %s %s" % (test_image_repo, test_image_path, cwd))
        os.system("docker run -it --rm  %s" % test_image_repo)
    except Exception, e:
        log.red("Failed to test with docker, because of %s" % e.message)


def publish(publish_image_name=None):
    application_conf = ApplicationConf.parse_application_conf()
    if publish_image_name == None:
        publish_image_name = application_conf.get("publish_image_name")
    try:
        cwd = os.getcwd()
        dockerfile_path = os.path.join(cwd, "Dockerfile")
        os.system("docker build -t %s -f %s %s" % (publish_image_name, dockerfile_path, cwd))
        os.system("docker push %s" % publish_image_name)
    except Exception, e:
        log.red("Failed to run with docker,because of %s" % e.message)


def serve():
    application_conf = ApplicationConf.parse_application_conf()
    publish_image_name = application_conf.get("publish_image_name")
    try:
        publish(publish_image_name)
        os.system("docker-compose up")
    except Exception, e:
        log.red("Failed to run with docker,because of %s" % e.message)
