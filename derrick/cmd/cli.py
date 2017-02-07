from docopt import docopt
import convert
import deploy
import local


class Cli:
    DERRICK_VERSION = "0.0.1"

    DERRICK_HELP = """
    Usage:
        derrick install <platform-git-repo>
        derrick init [<platform>]
        derrick test
        derrick publish
        derrick serve
        derrick deploy

    Options:
      -h --help         # Print this info and generator's options and usage
      -v --version      # Print version

    """

    # install a language module
    # you can specific a git branch or tag in commands args
    # such as:
    #      derrick install git@github.com:***/buildpack-go.git v2
    # if module version is not designated
    # the master branch will be the default choice
    def install(self, arguments=None):
        platform = arguments.get("<platform-git-repo>")
        local.install(platform)

    # detect current language framework and dependencies
    # a buildpack module named such as buildpack-nodejs
    # and you can use nodejs as platform in commands line
    def init(self, arguments=None):
        platform = arguments.get("<platform>")
        convert.convert(platform)

    # build Dockerfile.test in path
    # and run unittests in local containers
    def test(self, arguments=None):
        local.test()

    # build docker image in local
    # and publish image to aliyun docker hub service
    def publish(self, arguments=None):
        local.publish()

    # serve docker containers in local
    # using the docker-compose.yml in path
    def serve(self, arguments=None):
        local.serve()

    # Deploy application using the docker-compose file in path
    def deploy(self, arguments=None):
        deploy.deploy()

    def has_commands(self, key):
        try:
            action_handler = getattr(self, key)
            return True, action_handler
        except Exception, e:
            return False, None

    def run(self):
        arguments = docopt(Cli.DERRICK_HELP, help=False, version=Cli.DERRICK_VERSION)
        for key in arguments:
            exists, handler = self.has_commands(key)
            if arguments.get(key) == True and exists == True:
                handler(arguments=arguments)
