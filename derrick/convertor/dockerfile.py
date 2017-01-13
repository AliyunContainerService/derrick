"""

    2017.01.09
    dockerfile convertor

"""

from jinja2 import Template
import os


class DockerfileConvertor():
    def __init__(self, base_image, dockerfile_commands, start_commands, test_commands):
        self.base_image = base_image
        self.dockerfile_commands = dockerfile_commands
        self.start_commands = start_commands
        self.test_commands = test_commands

    def convert(self, dockerfile_template=None, dockerfile_test_template=None):
        cwd = os.getcwd()
        dockerfile_path = os.path.join(cwd, "Dockerfile")
        dockerfile_test_path = os.path.join(cwd, "Dockerfile.test")
        # composefile_path = os.path.join(cwd, "docker-compose.yml")

        if dockerfile_template != None:
            with open(dockerfile_path, "wa") as file:
                template = Template(dockerfile_template)
                content = template.render(base_image=self.base_image, commands=self.dockerfile_commands,
                                          start_commands=self.start_commands)
                file.write(content)
                file.close()
        if dockerfile_test_template != None:
            with open(dockerfile_test_path, "wa") as file:
                template = Template(dockerfile_test_template)
                content = template.render(base_image=self.base_image, commands=self.dockerfile_commands,
                                          test_commands=self.test_commands)
                file.write(content)
                file.close()
