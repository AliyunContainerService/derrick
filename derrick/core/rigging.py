#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.extension import ExtensionPoint


class Rigging(ExtensionPoint):
    """
    The main purpose of a Rigging is to fill the blank that defined
    in your templates such as Dockerfile or some other config Template.

    """
    def detect(self):
        pass

    def compile(self):
        pass
