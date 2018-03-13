#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
[COMMANDS_DOC_SECTION]
    derrick --version
Options:
    -d    Set debug mode
"""
from __future__ import absolute_import, division, print_function

from docopt import docopt

from derrick.core.command import CommandContext
from derrick.core.command_manager import CommandManager
from derrick.core.common import *
from derrick.core.engine_manager import EngineManager
from derrick.core.logger import Logger
from derrick.core.rigging_manager import RiggingManager
from derrick.core.recorder import DerrickRecorder


@singleton
class Derrick(object):
    """
    Derrick is a singleton in the whole lifecycle
    It will proxy command execution to commands_manager
    And Derrick will collect all commands status and result
    If the result or status is useful and it will save them
    to derrick_conf file in the application folder.
    """

    def __init__(self):
        self.cm = CommandManager()
        self.cm.set_commands_doc_template(__doc__)
        self.rm = RiggingManager()
        self.em = EngineManager()
        self.recorder = DerrickRecorder()

    # First time to run Derrick
    # create .derrick and .derrick/rigging in user root path
    # copy built-in rigging to .derrick/rigging
    def pre_load(self):
        os.mkdir(get_derrick_home())
        os.mkdir(get_rigging_home())
        os.mkdir(get_commands_home())
        Logger.info(DERRICK_LOGO)
        Logger.info("This is the first time to run Derrick.\n")
        Logger.info("Successfully create DERRICK_HOME in %s" % (get_derrick_home()))

    def load(self):
        if check_derrick_first_setup() is True:
            try:
                self.pre_load()
            except Exception as e:
                Logger.error("Failed to create DERRICK_HOME:%s.Because of %s" % (get_derrick_home(), e))
                # Logger.debug(traceback.format_exc())
                return
        # Load rigging and commands in disk
        self.rm.load()
        self.cm.load()
        self.em.load()

    def run(self):
        try:
            self.load()
        except Exception as e:
            # TODO add some exception handler
            Logger.error("Failed to load rigging or commands in disk,because of %s" % e)

        commands_doc = self.cm.get_commands_doc()
        arguments = docopt(commands_doc, help=False, version=DERRICK_VERSION)
        if DEBUG_MODE in arguments and arguments[DEBUG_MODE] == 1:
            Logger.set_debug_mode()

        # if not config command and check record valid
        if arguments["config"] is False:
            if self.recorder.is_valid() is False:
                Logger.error("Your should run `derrick config` first")
                return

        command_context = self.init_commands_context(arguments=arguments)
        self.cm.run_commands(command_context)

    def get_commands_manager(self):
        return self.cm

    def get_rigging_manager(self):
        return self.rm

    def get_engine_manager(self):
        return self.em

    def get_recorder(self):
        return self.recorder

    def init_commands_context(self, arguments):
        """
        set some useful information to context
        such as DERRICK_HOME and so on.
        """
        context = CommandContext()
        context.set(DERRICK_HOME_ENV, get_derrick_home())
        context.set(WORKSPACE_ENV, os.getcwd())
        context.set_arguments(arguments)
        return context
