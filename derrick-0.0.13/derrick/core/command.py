#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from derrick.core.extension import ExtensionPoint

COMMAND_NOT_IMPLEMENTED_EXCEPTION = "The specific command doesn't implement the `%s` function."


class Command(ExtensionPoint):
    # get command name by class name
    def __init__(self):
        self.name = self.__class__.__name__.lower()

    # execute the command with a context
    def execute(self, context):
        raise NotImplementedError(COMMAND_NOT_IMPLEMENTED_EXCEPTION % "execute")

    # docopt will combine all the desc to one single help
    def get_help_desc(self):
        raise NotImplementedError(COMMAND_NOT_IMPLEMENTED_EXCEPTION % "get_help_desc")


class CommandContext(dict):
    """
    set some common context envs to command
    """

    def __init__(self):
        super(CommandContext, self).__init__()

    def set(self, key, value):
        self[key] = value

    def get(self, key):
        return self[key]

    def set_arguments(self, arguments):
        self["arguments"] = arguments

    def get_arguments(self):
        return self["arguments"]
