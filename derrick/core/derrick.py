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

import os

from docopt import docopt

import derrick.core.logger as log
from derrick.core.command import CommandContext
from derrick.core.command_manager import CommandManager
from derrick.core.common import *
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
        self.rm = RiggingManager()

    # First time to run Derrick
    # create .derrick and .derrick/rigging in user root path
    # copy built-in rigging to .derrick/rigging
    def pre_load(self):
        try:
            os.mkdir(self.get_derrick_home())
            os.mkdir(self.get_rigging_home())
            os.system("cp -r %s/* %s" % (self.get_built_in_rigging_path(), self.get_rigging_home()))
            log.info(DERRICK_LOGO)
            log.info("This is the first time to run Derrick.\n")
            log.info("Successfully create DERRICK_HOME in %s" % (self.get_derrick_home()))
        except Exception as e:
            log.error("Failed to create DERRICK_HOME:%s.Because of %s" % (self.get_derrick_home(), e.message))
            return
        return

    # load all rigging and application conf
    def load(self):
        if self.check_first_setup() == True:
            try:
                self.pre_load()
            except Exception as e:
                log.error(e.message)
                return
        # load RiggingManager
        self.rm.load()

        # load CommandManager
        self.cm.set_commands_doc_template(__doc__)
        self.cm.load()

        return

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

    def get_built_in_rigging_path(self):
        derrick_source_path = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
        return os.path.join(derrick_source_path, DERRICK_BUILT_IN)

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
