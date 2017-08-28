#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
[COMMANDS_DOC_SECTION]
    derrick -h | --help
    derrick -d | --debug
    derrick --version
Options:
    -d --debug   Set debug mode
    -h --help    Show derrick help
    --version    Show derrick version
"""
from __future__ import absolute_import, division, print_function
from derrick.core.command_manager import CommandManager
from derrick.core.command import CommandContext
from derrick.core.common import singleton
from docopt import docopt
import derrick.core.logger as log
import os

DERRICK_LOGO = """
    8888888b.                       d8b        888
    888  "Y88b                      Y8P        888
    888    888                                 888
    888    888 .d88b. 888d888888d888888 .d8888b888  888
    888    888d8P  Y8b888P"  888P"  888d88P"   888 .88P
    888    88888888888888    888    888888     888888K
    888  .d88PY8b.    888    888    888Y88b.   888 "88b
    8888888P"  "Y8888 888    888    888 "Y8888P888  888

    ===================================================
    Derrick is a scaffold tool to migrate applications
    You can use Derrick to migrate your project simply.
    ===================================================
"""
DERRICK_HOME = "DERRICK_HOME"
RIGGING_HOME = "rigging"
DEBUG_MODE = "debug"
WORKSPACE = "WORKSPACE"


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
        self.cm.load()

    def pre_load(self):
        """
        First time to run Derrick
        create .derrick and .derrick/rigging in user root path
        copy built-in rigging to .derrick/rigging
        :return:
        """
        try:
            os.mkdir(self.get_derrick_home())
            os.mkdir(self.get_rigging_home())
            log.info(DERRICK_LOGO)
            log.info("This is the first time to run Derrick.\n")
            log.info("Successfully create DERRICK_HOME in %s" % (self.get_derrick_home()))
        except Exception as e:
            log.error("Failed to create DERRICK_HOME:%s.Because of %s" % (self.get_derrick_home(), e.message))
            return
        return

    def load(self):
        if self.check_first_setup() == True:
            try:
                self.pre_load()
            except Exception as e:
                log.error(e.message)
                return
        return

        # Entry Point

    def run(self):
        try:
            self.load()
        except Exception as e:
            # TODO add some exception handler
            print(e.message)

        commands_doc = self.cm.get_commands_doc()
        arguments = docopt(commands_doc, help=False, version="0.0.1")
        # set debug mode if necessary
        if arguments[DEBUG_MODE] == True:
            log.set_debug_mode()

        # construct command context and pass some useful message to command
        command_context = CommandContext()
        self.set_application_env(context=command_context)
        command_context.set_arguments(arguments)

        # run commands with context
        self.cm.run_commands(command_context)

    def get_derrick_home(self):
        env_home = os.getenv(DERRICK_HOME)
        if env_home != None:
            return env_home
        else:
            return os.path.join(os.path.expanduser("~"), ".derrick")

    def get_rigging_home(self):
        derrick_home = self.get_derrick_home()
        return os.path.join(derrick_home, "rigging")

    def get_rigging_home(self):
        return os.path.join(self.get_derrick_home(), RIGGING_HOME)

    # when you need to load custom user's command
    def get_commands_manager(self):
        return self.cm

    # check if derrick is used for the first time.
    def check_first_setup(self):
        derrick_home = self.get_derrick_home()

        if not os.path.exists(derrick_home):
            return True
        return False

    # set some useful information to context such derrick_home and so on.
    def set_application_env(self, context):
        context.set(DERRICK_HOME, self.get_derrick_home())
        context.set(WORKSPACE, os.getcwd())
