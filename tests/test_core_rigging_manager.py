#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
from derrick.core.rigging_manager import RiggingManager
import unittest


class RiggingManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.rm = RiggingManager()

    def test_rigging_manager_load(self):
        self.rm.load()
        modules = self.rm.all()
        print(modules)