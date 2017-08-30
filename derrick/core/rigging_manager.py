#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.common import *
from derrick.core.extension import ExtensionPoints
from derrick.core.module_loader import RiggingModuleLoader


class RiggingManager(ExtensionPoints):
    def __init__(self):
        super(RiggingManager, self).__init__()
        rigging_home = get_rigging_home()
        self.rigging_module_loader = RiggingModuleLoader(rigging_home)

    def load(self, rigging_name=None):
        modules = self.rigging_module_loader.load(rigging_name)
        if modules != None:
            for module in modules:
                self.register(module)
