#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Detector(object):
    def execute(self, *args, **kwargs):
        raise NotImplementedError("The specific detector execute function is not implemented.")
