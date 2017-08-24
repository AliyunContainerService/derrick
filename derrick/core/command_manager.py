#! /usr/bin/env python
# -*- coding: utf-8 -*-
from derrick.core.extension import ExtensionPoints
from derrick.commands import *


class CommandManager(ExtensionPoints):
    """
    manage all commands from CommandManager
    """

    # direct load from derrick
    def load(self):
        self.register(Init())
        self.register(Build())
        self.register(Test())


class CommandContext(object, dict):
    """
    set some common context envs to command
    """
    pass
