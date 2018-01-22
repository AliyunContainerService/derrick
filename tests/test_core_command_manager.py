#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest
from derrick.core.command_manager import CommandManager
from derrick.core.command import Command
from derrick.core.derrick import Derrick


class CommandManagerTestCase(unittest.TestCase):
    def setUp(self):
        # pre load
        derrick = Derrick()
        derrick.load()

        self.cm = CommandManager()
        self.cm.load()

    def test_built_in_commands(self):
        built_in_commands_num = len(self.cm.all().keys())
        self.assertEquals(3, built_in_commands_num)

    def test_built_in_commands_registered(self):
        commands_dict = self.cm.all()
        self.assertIsNot(None, commands_dict["up"])
        self.assertIsNot(None, commands_dict["init"])

    def test_built_int_commands_re_registration(self):
        class Build(Command):
            pass

        custom_build = Build()

        # overwrite a command if necessary
        self.cm.register(custom_build)

        all_commands = self.cm.all()

        self.assertEquals(True, all_commands["build"] is custom_build)
    def test_command_manager_template(self):
        template = "Test CommandManager Template"
        self.cm.set_commands_doc_template(template)
        template_replace = self.cm.get_commands_doc()
        self.assertEqual(template,template_replace)