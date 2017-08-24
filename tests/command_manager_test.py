#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


import unittest
from derrick.core.command_manager import CommandManager


class CommandManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.cm = CommandManager()

    def tearDown(self):
        self.cm = None

    def test_default_commands_load(self):
        commands = self.cm.all()
        print(commands)
