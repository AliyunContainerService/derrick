#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import unittest

from derrick.detectors.image.golang import GolangVersionDetector


class GolangTestCase(unittest.TestCase):
    def test_golang_detector(self):
        gr = GolangVersionDetector()
        version = gr.execute()
        print("golang version detected %s" % version)
        self.assertIsNotNone(version)
