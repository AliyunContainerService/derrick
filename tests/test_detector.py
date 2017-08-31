#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.detectors.image.node import NodeVersionDetector


class DetectorTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_nodejs_version(self):
        node_version_detector = NodeVersionDetector()
        version = node_version_detector.execute()
        self.assertEqual(True, version is not None)
