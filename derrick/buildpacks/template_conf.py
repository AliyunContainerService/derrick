"""
    Supply some utils func to operate template key map
"""


class TemplateConf:
    def __init__(self, conf=None):
        self.conf = conf or {}

    # unshift a key to template key map
    def unshift(self, key, item):
        arr = self.__exists_or_create(key)
        arr = item + arr
        self.conf[key] = arr

    # append a key to template key map
    def append(self, key, item):
        arr = self.__exists_or_create(key)
        arr = arr + item
        self.conf[key] = arr

    # override value in template key map
    def set(self, key, value):
        self.__exists_or_create(key)
        self.conf[key] = value

    # return tempalte conf
    def get_conf(self):
        return self.conf

    # update and return merge new conf
    def update(self, new_conf):
        for key in new_conf:
            new_value = new_conf.get(key)

            if type(self.conf.get(key)) == list:
                self.append(key, new_value)
            else:
                self.set(key, new_value)

        return self.conf

    # private func to check or create key and value in template map
    def __exists_or_create(self, key):
        arr = self.conf.has_key(key) and self.conf[key] or []
        if arr == None or type(arr) != list:
            arr = []
        return arr


"""

Dockerfile template structure

-----------------

FROM [BASE_IMAGE]

[PRE_BLOCK]

RUN [PRE_COMMANDS]

RUN [COMMANDS]

RUN [POST_COMMANDS]

[POST_BLOCK]

CMD [START_COMMANDS]

--------------------

"""

SPLIT_ENTER = "\n"
SPLIT_ENTER_WITH_AND = "\\\n&&  "


class DockerfileTemplateConf(TemplateConf):
    BASE_IMAGE = "base_image"

    PRE_BLOCK = "pre_block"
    POST_BLOCK = "post_block"

    PRE_COMMANDS = "pre_commands"
    COMMANDS = "commands"
    POST_COMMANDS = "post_commands"

    START_COMMANDS = "start_commands"
    TEST_COMMANDS = "test_commands"

    def __get_keys_from_conf(self, *args):
        values = []
        for key in args:
            values.append(self.conf.get(key) or [])
        return tuple(values)

    def convert_commands(self, commands):
        return SPLIT_ENTER_WITH_AND.join(commands)

    def convert_block(self, block):
        return SPLIT_ENTER.join(block)

    def convert_endpoint_commands(self, commands):
        return str(commands).replace("\'", "\"")

    def convert_to_template_conf(self):
        convert_conf = {}
        base_image = self.conf.get(DockerfileTemplateConf.BASE_IMAGE)
        pre_block, post_block = self.__get_keys_from_conf(DockerfileTemplateConf.PRE_BLOCK,
                                                          DockerfileTemplateConf.POST_BLOCK)
        pre_commands, commands, post_commands = self.__get_keys_from_conf(DockerfileTemplateConf.PRE_COMMANDS,
                                                                          DockerfileTemplateConf.COMMANDS,
                                                                          DockerfileTemplateConf.POST_COMMANDS)
        start_commands, test_commands = self.__get_keys_from_conf(DockerfileTemplateConf.START_COMMANDS,
                                                                  DockerfileTemplateConf.TEST_COMMANDS)

        # update base_image conf
        convert_conf.update({
            DockerfileTemplateConf.BASE_IMAGE: base_image,
        })

        # update pre and post block
        convert_conf.update({
            DockerfileTemplateConf.PRE_BLOCK: self.convert_block(pre_block),
            DockerfileTemplateConf.POST_BLOCK: self.convert_block(post_block),
        })

        # update pre and post commands
        convert_conf.update({
            DockerfileTemplateConf.PRE_COMMANDS: self.convert_commands(pre_commands),
            DockerfileTemplateConf.COMMANDS: self.convert_commands(commands),
            DockerfileTemplateConf.POST_COMMANDS: self.convert_commands(post_commands),
        })

        # update commands
        convert_conf.update({
            DockerfileTemplateConf.START_COMMANDS: self.convert_endpoint_commands(start_commands),
            DockerfileTemplateConf.TEST_COMMANDS: self.convert_endpoint_commands(test_commands),
        })

        return convert_conf


class DockerComposeTemplateConf(TemplateConf):
    def convert_to_template_conf(self):
        convert_conf = self.conf
        ports = self.conf.get('ports')
        ports_arr = ports.split(" ")
        convert_conf.update({
            "ports": ports_arr,
        })
        return convert_conf
