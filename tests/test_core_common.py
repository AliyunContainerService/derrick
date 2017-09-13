#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.core.common import *


class CommonTestCase(unittest.TestCase):
    def test_get_rigging_home(self):
        derrick_home = get_derrick_home()
        rigging_home = get_rigging_home()
        self.assertEquals(rigging_home, os.path.join(derrick_home, RIGGING_HOME))
