#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.rigging import Rigging

PLATFORM = "Python"


class PythonRigging(Rigging):
    def detect(self, context):
        return False, None

    def compile(self, context):
        return
