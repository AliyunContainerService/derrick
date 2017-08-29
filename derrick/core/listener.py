#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.extension import ExtensionPoint


class Listener(ExtensionPoint):
    def get_name(self):
        pass
