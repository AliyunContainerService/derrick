import simplejson as json
import chalk as log
import os
import conf


class ApplicationConf(conf.Configuration):
    @staticmethod
    def init_application_conf(conf):
        application_conf_path = ApplicationConf.get_application_conf_path()
        try:
            file = open(application_conf_path, "w")
            json.dump(conf, file, indent=4)
            return conf
        except Exception, e:
            log.red("Failed to load application conf in cwd path, because of %s" % e.message)

    @staticmethod
    def update_application_conf(conf):
        application_conf = ApplicationConf.parse_application_conf() or {}
        application_conf_path = ApplicationConf.get_application_conf_path()
        try:
            application_conf.update(conf)
            file = open(application_conf_path, "w")
            json.dump(application_conf, file, indent=4)
        except Exception, e:
            log.red("Failed to update_application_conf,because of %s" % e.message)

    @staticmethod
    def parse_application_conf():
        application_conf_path = ApplicationConf.get_application_conf_path()
        try:
            file_data = open(application_conf_path).read()
            json_data = json.loads(file_data)
            return json_data
        except Exception, e:
            log.red("Failed to parse application conf,because of %s" % e.message)

    @staticmethod
    def get_application_conf_path():
        cwd = os.getcwd()
        application_conf_path = os.path.join(cwd, "derrick_application.json")
        return application_conf_path
