#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from derrick.core.common import *
from derrick.core.extension import ExtensionPoints
from derrick.core.logger import Logger
from derrick.core.module_loader import CommandModuleLoader

NEW_LINE = "\n"
FOUR_WHITESPACE = "    "
COMMANDS_DOC_SECTION = "[COMMANDS_DOC_SECTION]"


class CommandManager(ExtensionPoints):
    """
    manage all commands from CommandManager
    """

    def __init__(self):
        super(CommandManager, self).__init__()
        derrick_commands_home = get_commands_home()
        self.cl = CommandModuleLoader(derrick_commands_home)

    # direct load from derrick
    def load(self):
        commands = self.cl.load()
        for command in commands:
            self.register(command)

    def set_commands_doc_template(self, template):
        self.template = template

    def get_commands_doc(self):
        commands = self.all()
        commands_help_doc_arr = []
        for command in commands.values():
            commands_help_doc_arr.append(FOUR_WHITESPACE + command.get_help_desc())
        commands_help_desc = NEW_LINE.join(commands_help_doc_arr)
        commands_doc = self.template.replace(COMMANDS_DOC_SECTION, commands_help_desc)
        return commands_doc

    def run_commands(self, context):
        commands = self.all()
        arguments = context.get_arguments()
        for command_name in commands.keys():
            if arguments[command_name] == True:
                command = commands[command_name]
                try:
                    command.execute(context)
                except Exception as e:
                    Logger.error(e.message)
        return
