#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import traceback

from derrick.core.common import *
from derrick.core.extension import ExtensionPoints
from derrick.core.logger import Logger
from derrick.core.module_loader import CommandModuleLoader


class CommandManager(ExtensionPoints):
    """
    CommandManager extends ExtensionPoints
    CommandManager load built-in commands and user custom commands
    CommandManager is the actual command manager and executor
    """
    template = ""

    def __init__(self):
        super(CommandManager, self).__init__()
        derrick_commands_home = get_commands_home()
        self.cl = CommandModuleLoader(derrick_commands_home)

    def load(self):
        """
        Load built-in commands and developer's custom commands
        Your can simply extends derrick.core.command.Command
        And put them in DERRICK_HOME/commands then Derrick
        will auto-load your commands.

        Maybe you can define a command which can deploy to K8S.
        """
        import derrick.commands.up as u
        import derrick.commands.init as i
        import derrick.commands.config as c
        self.register(u.Up())
        self.register(i.Init())
        self.register(c.Config())

        commands = self.cl.load()
        for command in commands:
            self.register(command)

    # docopt commands options and usage
    def set_commands_doc_template(self, template):
        self.template = template

    # construct commands usage and options from the command registered.
    def get_commands_doc(self):
        commands = self.all()
        commands_help_doc_arr = []
        for command in commands.values():
            commands_help_doc_arr.append(FOUR_WHITESPACE + command.get_help_desc())
        commands_help_desc = NEW_LINE.join(commands_help_doc_arr)
        commands_doc = self.template.replace(COMMANDS_DOC_SECTION, commands_help_desc)
        return commands_doc

    def run_commands(self, context):
        # if you define a command that has the same name with others
        # the latest registered command will execute 
        commands = self.all()
        arguments = context.get_arguments()
        for command_name in commands.keys():
            command_name_lower = command_name.lower()
            if command_name_lower in arguments.keys() and arguments[command_name_lower] is True:
                command = commands[command_name]
                try:
                    command.execute(context)
                    # TODO Add command event listener in here
                    # TODO event listener will fire event in the whole lifecycle
                except Exception as e:
                    Logger.error("Failed to execute command %s,because of %s" % (command_name, e))
                    Logger.debug(traceback.format_exc())
