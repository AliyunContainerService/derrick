"""

    2016.01.09
    Commands Interface

"""

DERRICK_SLOGAN = """
8888888b.                       d8b        888
888  "Y88b                      Y8P        888
888    888                                 888
888    888 .d88b. 888d888888d888888 .d8888b888  888
888    888d8P  Y8b888P"  888P"  888d88P"   888 .88P
888    88888888888888    888    888888     888888K
888  .d88PY8b.    888    888    888Y88b.   888 "88b
8888888P"  "Y8888 888    888    888 "Y8888P888  888

===================================================
 Derrick is a project scaffold for Docker Developer
 Current Version is %s
===================================================

"""

"""
//后续开放如下命令
    derrick test
    derrick publish
    derrick serve
    derrick deploy
"""

DERRICK_HELP = """
Usage:
    derrick install <platform-git-repo>
    derrick init [<platform>]


Options:
  -h --help         # Print this info and generator's options and usage
  -v --version      # Print version

"""

DERRICK_VERSION = "0.0.1"

from docopt import docopt
import convert
import deploy
import local


class Cli:
    def __init__(self):
        pass

    def has_commands(self, key):
        try:
            action_handler = getattr(self, key)
            return True, action_handler
        except Exception, e:
            return False, None

    def run(self):
        # print(DERRICK_SLOGAN % DERRICK_VERSION)
        arguments = docopt(DERRICK_HELP, help=False, version=DERRICK_VERSION)
        for key in arguments:
            exists, handler = self.has_commands(key)
            if arguments.get(key) == True and exists == True:
                handler(arguments=arguments)

    def install(self, arguments=None):
        platform = arguments.get("<platform-git-repo>")
        local.install(platform)

    def init(self, arguments=None):
        platform = arguments.get("<platform>")
        convert.convert(platform)

    def test(self, arguments=None):
        local.test()

    def publish(self, arguments=None):
        local.publish()

    def serve(self, arguments=None):
        local.serve()

    def deploy(self, arguments=None):
        deploy.deploy()
