#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from detectors.image.php import PhpVersionDetector


class PhpVersionTestCase(unittest.TestCase):
    def test_version(self):
        pd = PhpVersionDetector()
        version = pd.execute()
        print(version)
        self.assertIsNotNone(version)
