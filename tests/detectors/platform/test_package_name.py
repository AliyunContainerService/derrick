#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.detectors.platform.golang.package_name import PackageNameDetector


@unittest.skip("skip if not golang project")
class PackageNameTestCase(unittest.TestCase):
    def test_package_name_detector(self):
        gr = PackageNameDetector()
        gpm = gr.execute()
        self.assertIsNotNone(gpm)
