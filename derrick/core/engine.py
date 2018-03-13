#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.extension import ExtensionPoint


class Engine(ExtensionPoint):
    # Return Engine class name as unique index
    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def up(self, *args, **kwargs):
        raise NotImplementedError("Every engine should implement this method!")
