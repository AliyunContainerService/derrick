#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

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


class CommandContext(object):
    """
    set some common context envs to command
    """
    pass
