#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.core.common import *
from derrick.core.derrick import Derrick


class DerrickTest(unittest.TestCase):
    def setUp(self):
        self.dk = Derrick()

    def test_singleton_derrick(self):
        dk1 = Derrick()
        dk2 = Derrick()
        self.assertEquals(True, dk1 is dk2)

    def test_get_derrick_home(self):
        home = get_derrick_home()
        predicted_home = os.path.join(os.path.expanduser("~"), ".derrick")
        self.assertEqual(home, predicted_home)

    @unittest.skip("skip env test")
    def test_get_derrick_home_with_env(self):
        env_home = "/root/.derrick"
        os.putenv(DERRICK_HOME, env_home)
        home = get_derrick_home()
        predicted_home = env_home
        self.assertEqual(home, predicted_home)
        os.unsetenv(DERRICK_HOME)

    def test_derrick_home(self):
        derrick_home = get_derrick_home()
        if os.path.exists(derrick_home) is True:
            self.assertEqual(check_derrick_first_setup(), False)
            return
        self.assertEqual(check_derrick_first_setup(), True)
        self.dk.pre_load()
        self.assertEqual(check_derrick_first_setup(), False)
