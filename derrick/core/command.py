#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from derrick.core.extension import ExtensionPoint

COMMAND_NOT_IMPLEMENTED_EXCEPTION = "The specific command doesn't implement the `%s` function."


class Command(ExtensionPoint):
    # get command name by class name
    def __init__(self):
        self.name = self.__class__.__name__

    # execute the command with a context
    def execute(self, context):
        raise NotImplementedError(COMMAND_NOT_IMPLEMENTED_EXCEPTION % "execute")

    # docopt will combine all the desc to one single help
    def get_help_desc(self, context):
        raise NotImplementedError(COMMAND_NOT_IMPLEMENTED_EXCEPTION % "get_help_desc")




