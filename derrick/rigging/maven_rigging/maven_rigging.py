#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.rigging import Rigging
from derrick.detectors.image.java import JavaVersionDetector
from derrick.core.detector_report import DetectorReport

RUNTIME = "Maven"


class MavenRigging(Rigging):
    def detect(self, context):
        """
        :param context:
        :return: handled(bool),platform(string)
        """
        workspace = context.get("WORKSPACE")
        package_json_file = os.path.join(workspace, "pom.xml")
        if os.path.exists(package_json_file) is True:
            return True, RUNTIME
        return False, None

    def compile(self, context):
        dr = DetectorReport()
        docker_node = dr.create_node("Dockerfile.j2")
        docker_node.register_detector(JavaVersionDetector())
        return dr.generate_report()
