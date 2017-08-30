#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import inspect
import os
import sys

from derrick.core.command import Command
from derrick.core.extension import ExtensionPoint
from derrick.core.rigging import Rigging


class Module(ExtensionPoint):
    def __init__(self, module_name, module_class):
        self.module_name = module_name
        self.module_class = module_class

    def get_name(self):
        return self.module_name

    def load(self):
        return self.module_class()


class PathModuleLoader(object):
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
            modules.extend(self.load_module(os.path.join(self.path, module_name)))
        else:
            dirs = os.listdir(self.path)
            for module_path in dirs:
                if self.is_can_load(module_path) == False:
                    continue
                modules_arr = self.load_module(os.path.join(self.path, module_path))
                if len(modules_arr) == 0:
                    continue
                else:
                    modules.extend(modules_arr)
        return modules

    def load_module(self, path):
        if os.path.isdir(path) == False:
            path = os.path.dirname(path)
        sys.path.append(path)

        module_arr = []
        module_name = os.path.basename(path)
        module = __import__(module_name)
        for name, module_class in inspect.getmembers(module):
            if inspect.isclass(module_class) and \
                    issubclass(module_class, self.base_module) \
                    and (module_class.__bases__ == self.base_module.__bases__):
                module_arr.append(Module(module_name, module_class))
        return module_arr

    def is_can_load(self, path):
        if os.path.isdir(path) == True:
            return True
        if not str(path).endswith(".py") or str(path) == "__init__.py":
            return False
        return True


# TODO MultiPathModuleLoader
class MultiPathModuleLoader(PathModuleLoader):
    """
    MultiPathModuleLoader is useful when we need to debug or develop a rigging
    or create a custom commands
    """
    pass


# ModuleLoader for Rigging
class RiggingModuleLoader(PathModuleLoader):
    def __init__(self, path):
        super(RiggingModuleLoader, self).__init__(path, Rigging)


# ModuleLoader for Command
class CommandModuleLoader(PathModuleLoader):
    def __init__(self, path):
        super(CommandModuleLoader, self).__init__(path, Command)
