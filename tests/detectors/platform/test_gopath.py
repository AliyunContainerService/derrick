#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.detectors.platform.golang.gopath import GopathDetector


@unittest.skip
class TestGopathetector(unittest.TestCase):
    def test_gopath_detector(self):
        gr = GopathDetector()
        gph = gr.execute()
        self.assertIsNot(gph, None)
