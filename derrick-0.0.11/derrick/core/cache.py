#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.common import *


@singleton
class CacheStore(object):
    store = dict()

    def put(self, key, value):
        self.store[key] = value

    def get(self, key):
        try:
            return self.store[key]
        except Exception as e:
            return None
