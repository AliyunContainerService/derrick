#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import inspect
import os
import sys

from derrick.core.command import Command
from derrick.core.rigging import Rigging


class ModuleLoader(object):
    """
    ModuleLoader is a plugin classloader for Derrick
    It will help to load rigging, commands, listeners and so on.
    """

    def __init__(self, path, base_module):
        self.path = path
        self.base_module = base_module

    def load(self, module_name=None):
        modules = []
        if module_name != None:
            modules.append(self.load_module(os.path.join(self.path, module_name)))
        else:
            dirs = os.listdir(self.path)
            for module_path in dirs:
                module_map = self.load_module(os.path.join(self.path, module_path))
                if module_map == None:
                    continue
                else:
                    modules.append(module_map)
        return modules

    def load_module(self, path):
        sys.path.append(path)
        module_name = os.path.basename(path)
        module = __import__(module_name)
        for name, module_class in inspect.getmembers(module):
            if inspect.isclass(module_class) and \
                    issubclass(module_class, self.base_module) \
                    and (module_class.__bases__ == self.base_module.__bases__):
                return {module_name: module_class}
        return None


# ModuleLoader for Rigging
class RiggingModuleLoader(ModuleLoader):
    def __init__(self, path):
        super(RiggingModuleLoader, self).__init__(path, Rigging)


# ModuleLoader for Command
class CommandModuleLoader(ModuleLoader):
    def __init__(self, path):
        super(CommandModuleLoader, self).__init__(path, Command)
