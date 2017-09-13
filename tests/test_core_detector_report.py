#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import unittest

from derrick.core.detector_report import DetectorReport


class DetectorReportTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_single_node(self):
        dr = DetectorReport()
        node1 = dr.create_node("node1")
        node1.extend_content({"version": "1"})
        result_dict = dr.generate_report()

        self.assertEquals(1, len(result_dict.keys()))

    def test_multi_nodes(self):
        dr = DetectorReport()
        node1 = dr.create_node("node1")
        node1.extend_content({"version": "1.0"})
        node2 = dr.create_node("node2")
        node2.extend_content({"content": "content"})
        result_dict = dr.generate_report()

        self.assertEquals(2, len(result_dict.keys()))

    def test_complex_nodes(self):
        dr = DetectorReport()
        node1 = dr.create_node("node1")
        node1.extend_content({"version": "1.0"})
        node2 = node1.create_node("node2")
        node2.extend_content({"content": "content"})
        result_dict = dr.generate_report()

        self.assertEquals(1, len(result_dict.keys()))
        self.assertEquals("content", result_dict["node1"]["node2"]["content"])

    def test_override(self):
        dr = DetectorReport()
        node1 = dr.create_node("node1")
        node1.extend_content({"version": "1.0"})
        node1.extend_content({"version": "2.0"})
        result_dict = dr.generate_report()

        self.assertEquals("2.0", result_dict["node1"]["version"])
