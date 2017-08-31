#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.rigging import Rigging
from derrick.detectors.image.java import JavaVersionDetector

RUNTIME = "Maven"


class MavenRigging(Rigging):
    def detect(self, context):
        """
        :param context:
        :return: handled(bool),platform(string)
        """
        workspace = context.get("WORKSPACE")
        package_json_file = os.path.join(workspace, "pom.xml")
        if os.path.exists(package_json_file) == True:
            return True, RUNTIME
        return False, None

    def compile(self, context):
        java_version_detector = JavaVersionDetector()
        java_version = java_version_detector.execute()
        return {"Dockerfile.j2": {"version": java_version}}
