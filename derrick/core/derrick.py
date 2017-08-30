#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
[COMMANDS_DOC_SECTION]
    derrick -h | --help
    derrick --version
Options:
    -d --debug   Set debug mode
    -h --help    Show derrick help
    --version    Show derrick version
"""
from __future__ import absolute_import, division, print_function

from docopt import docopt

from derrick.core.command import CommandContext
from derrick.core.command_manager import CommandManager
from derrick.core.common import *
from derrick.core.logger import Logger as log
from derrick.core.rigging_manager import RiggingManager


@singleton
class Derrick(object):
    """
    Derrick is a singleton in the whole lifecycle
    It will proxy command execution to commands_manager
    And Derrick will collect all commands status and result
    If the result or status is useful and it will save them
    to .derrick_application file in the application folder.
    """

    def __init__(self):
        self.cm = CommandManager()
        self.cm.set_commands_doc_template(__doc__)
        self.rm = RiggingManager()

    # First time to run Derrick
    # create .derrick and .derrick/rigging in user root path
    # copy built-in rigging to .derrick/rigging
    def pre_load(self):
        try:
            os.mkdir(get_derrick_home())
            os.mkdir(get_rigging_home())
            os.system("cp -r %s/* %s" % (get_built_in_rigging_path(), get_rigging_home()))
            log.info(DERRICK_LOGO)
            log.info("This is the first time to run Derrick.\n")
            log.info("Successfully create DERRICK_HOME in %s" % (get_derrick_home()))
        except Exception as e:
            log.error("Failed to create DERRICK_HOME:%s.Because of %s" % (get_derrick_home(), e.message))
            return
        return

    # load all rigging and application conf
    def load(self):
        if self.check_derrick_first_setup() == True:
            try:
                self.pre_load()
            except Exception as e:
                log.error(e.message)
                return

        if self.check_application_first_setup() == True:
            self.rm.load()
        else:
            self.rm.load("rigging_name")

        # load CommandManager
        self.cm.load()

        return

    def run(self):
        try:
            self.load()
        except Exception as e:
            # TODO add some exception handler
            print(e.message)

        commands_doc = self.cm.get_commands_doc()
        arguments = docopt(commands_doc, help=False, version=DERRICK_VERSION)
        # set debug mode if necessary
        if arguments[DEBUG_MODE] == True:
            log.set_debug_mode()

        # construct command context and pass some useful message to command
        command_context = CommandContext()
        self.set_application_env(context=command_context)
        command_context.set_arguments(arguments)

        # run commands with context
        self.cm.run_commands(command_context)

    # when you need to load custom user's command
    def get_commands_manager(self):
        return self.cm

    def get_rigging_manager(self):
        return self.rm

    # check if derrick is used for the first time.
    def check_derrick_first_setup(self):
        derrick_home = get_derrick_home()
        if not os.path.exists(derrick_home):
            return True
        return False

    def check_application_first_setup(self):
        application_conf = os.path.join(os.getcwd(), ".derrick_application")
        if not os.path.exists(application_conf):
            return True
        return False

    # set some useful information to context such derrick_home and so on.
    def set_application_env(self, context):
        context.set(DERRICK_HOME, get_derrick_home())
        context.set(WORKSPACE, os.getcwd())

    @staticmethod
    def get_active_instance():
        return 1
