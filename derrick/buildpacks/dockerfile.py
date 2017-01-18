"""

    2017.01.09
    dockerfile convertor

"""
import os
from jinja2 import Template
from exception import NotFoundTemplateConf
from template_conf import DockerfileTemplateConf
import chalk as log


class Convertor():
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
    def __init__(self, template_conf=None, source_template=None, dest_template=None):
        if template_conf != None:
            self.df = DockerfileTemplateConf(template_conf)
            self.template_conf = self.df.convert_to_template_conf()
        self.source_template = source_template
        self.dest_template = dest_template

    def set_template_conf(self, template_conf_instance):
        if template_conf_instance != None and isinstance(template_conf_instance) == DockerfileTemplateConf:
            self.df = template_conf_instance
            self.template_conf = template_conf_instance.convert_to_template_conf()

    def flush_template_file_to_disk(self):
        try:
            with open(self.source_template) as source_template_file:
                template_content = source_template_file.read()
                content = self.convert_to_template_content(template_content)
                if self.dest_template != None and os.path.exists(self.dest_template):
                    with open(self.dest_template, "w") as dest_file:
                        dest_file.write(content)
                else:
                    raise NotFoundTemplateConf
        except NotFoundTemplateConf:
            log.red("Failed to convert dockerfile,because of not found tempalte conf")
