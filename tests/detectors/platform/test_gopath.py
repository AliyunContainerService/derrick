#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.detectors.platform.golang.gopath import GopathDetector


class GopathTestCase(unittest.TestCase):
    def test_gopath_detector(self):
        gr = GopathDetector()
        gopath = gr.execute()
        print(gopath)
        self.assertIsNotNone(gopath)
