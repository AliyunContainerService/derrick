#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.cache import CacheStore


class DetectorReport(object):
    """
    construct a dict with complex structure is very difficult
    especially when you need to construct the detect dict with
    many detectors.


    DEMO:

    {
        "Dockerfile.j2":{
            "version":"1.0"
            "content":"content"
        }
    }

    dr = DetectorReport()
    dockerfile_node = dr.create_node("Dockerfile.j2")
    dockerfile_node.extend_content({"version":"1.0"})
    dockerfile_node.extend_content({"content":"content"})

    report = dr.generate_report()

    """

    def __init__(self, name=None):
        self.name = name
        self.nodes = dict()
        self.store = dict()

    def get_name(self):
        return self.name

    def get_node(self, node_name):
        return self.nodes[node_name]

    def create_node(self, node_name):
        dr = DetectorReport(node_name)
        self.nodes[node_name] = dr
        return dr

    def extend_content(self, detect_content=None):
        self.store.update(detect_content)

    def register_detector(self, detector, *args, **kwargs):
        cs = CacheStore()
        key = detector.__class__.__name__
        value = cs.get(key)
        if value is None:
            result = detector.execute(*args, **kwargs)
            cs.put(key, result)
        else:
            result = value
        self.extend_content(result)

    def parse_report(self, report):
        DetectorReport.recursive_parse_store(self, report)

    @staticmethod
    def recursive_parse_store(detector_node, data):
        for key in data.keys():
            content = data[key]
            if type(content) is dict:
                node = detector_node.create_node(key)
                DetectorReport.recursive_parse_store(node, content)
            else:
                detector_node.extend_content({key: content})

    def generate_report(self):
        return DetectorReport.recursive_generate_store(self)

    @staticmethod
    def recursive_generate_store(report_node):
        nodes = report_node.nodes
        store = report_node.store
        if len(nodes.keys()) > 0:
            for node_name in nodes.keys():
                store[node_name] = dict()
                node_store = store[node_name]
                node_store_item = DetectorReport.recursive_generate_store(nodes[node_name])
                node_store.update(node_store_item)
            return store
        else:
            return report_node.store
