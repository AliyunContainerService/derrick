"""

    2017.01.09
    dockerfile convertor

"""
from jinja2 import Template
from exception import NotFoundTemplateConf
from template_conf import DockerfileTemplateConf, DockerComposeTemplateConf
import chalk as log


class Convertor(object):
    def __init__(self):
        # your should change the value of template_conf
        # when extends convertor class
        self.template_conf = {}

    def convert_to_template_content(self, file_content):
        template = Template(file_content)
        content = template.render(self.template_conf)
        return content


# simple extends the parent class .
class DockerfileConvertor(Convertor):
    def __init__(self, template_conf=None):
        super(DockerfileConvertor, self).__init__()
        if template_conf != None:
            self.df = DockerfileTemplateConf(template_conf)
            self.template_conf = self.df.convert_to_template_conf()

    def set_template_conf(self, template_conf_instance):
        if template_conf_instance != None and isinstance(template_conf_instance, DockerfileTemplateConf) == True:
            self.df = template_conf_instance
            self.template_conf = template_conf_instance.convert_to_template_conf()

    def flush_template_file_to_disk(self, source_template, dest_template):
        try:
            with open(source_template) as source_template_file:
                template_content = source_template_file.read()
                content = self.convert_to_template_content(template_content)
                if dest_template != None:
                    with open(dest_template, "w") as dest_file:
                        dest_file.write(content)
                else:
                    raise NotFoundTemplateConf
        except NotFoundTemplateConf:
            log.red("Failed to convert dockerfile,because of not found tempalte conf")


class DockerComposeConvertor(Convertor):
    def __init__(self, template_conf=None):
        super(DockerComposeConvertor, self).__init__()
        if template_conf != None:
            print template_conf
            self.df = DockerComposeTemplateConf(template_conf)
            self.template_conf = self.df.convert_to_template_conf()

    def flush_template_file_to_disk(self, source_template, dest_template):
        try:
            with open(source_template) as source_template_file:
                template_content = source_template_file.read()
                content = self.convert_to_template_content(template_content)
                if dest_template != None:
                    with open(dest_template, "w") as dest_file:
                        dest_file.write(content)
                else:
                    raise NotFoundTemplateConf
        except NotFoundTemplateConf:
            log.red("Failed to convert docker-compose,because of not found tempalte conf")
