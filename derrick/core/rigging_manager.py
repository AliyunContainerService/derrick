#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.common import *
from derrick.core.extension import ExtensionPoints
from derrick.core.module_loader import RiggingModuleLoader


class RiggingManager(ExtensionPoints):
    """
    RiggingManager will load,manage,execute rigging.
    You can define a custom rigging and just put them
    in the DERRICK_HOME/rigging.

    RiggingManager will load built-in rigging and developer's
    custom rigging in RIGGING_HOME.

    Just like the CommandManager.If your rigging has the same
    name with other rigging.The latest registered works
    """

    def __init__(self):
        super(RiggingManager, self).__init__()
        rigging_home = get_rigging_home()
        self.rigging_module_loader = RiggingModuleLoader(rigging_home)

    def load(self, rigging_name=None):
        # buildIn rigging
        from derrick.rigging.nodejs_rigging.nodejs_rigging import NodejsRigging
        from derrick.rigging.maven_rigging.maven_rigging import MavenRigging
        from derrick.rigging.python_rigging.python_rigging import PythonRigging
        from derrick.rigging.golang_rigging.golang_rigging import GolangRigging
        from derrick.rigging.php_rigging.php_rigging import PhpRigging

        self.register(NodejsRigging())
        self.register(MavenRigging())
        self.register(PythonRigging())
        self.register(GolangRigging())
        self.register(PhpRigging())

        # Load developer's custom rigging
        modules = self.rigging_module_loader.load(rigging_name)
        if modules is not None:
            for module in modules:
                self.register(module)
