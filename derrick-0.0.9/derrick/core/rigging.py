#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import inspect
import os

from derrick.core.extension import ExtensionPoint


class Rigging(ExtensionPoint):
    """
    The main purpose of a Rigging is to fill the blank that defined
    in your templates such as Dockerfile or some other config Template.

    """

    def get_template_dir(self):
        basedir = os.path.dirname(inspect.getfile(self.__class__))
        return os.path.join(basedir, "templates")

    def get_name(self):
        return self.__class__.__name__

    def detect(self, context):
        raise NotImplementedError()

    def compile(self, context):
        raise NotImplementedError()
