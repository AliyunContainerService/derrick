#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import unittest

from derrick.detectors.image.java import JavaVersionDetector

JAVA_9 = "9.0.1"
JAVA_8 = "1.8.0_161-b12"


class JavaTestCase(unittest.TestCase):
    def test_java_version_detect(self):
        version_9 = JavaVersionDetector.get_most_relative_version(JAVA_9)
        self.assertEqual("9", version_9)
        version_8 = JavaVersionDetector.get_most_relative_version(JAVA_8)
        self.assertEqual("8", version_8)
