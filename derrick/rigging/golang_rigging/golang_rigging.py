#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.detector_report import DetectorReport
from derrick.core.rigging import Rigging
from derrick.detectors.general.image_repo import ImageRepoDetector
from derrick.detectors.image.golang import GolangVersionDetector

GOLANG = "Golang"


class GolangRigging(Rigging):
    def detect(self, context):
        cwd = os.getcwd()
        for filename in os.listdir(cwd):
            if filename.endswith(".go"):
                return GOLANG, True
        return "", False

    def compile(self, context):
        dc = DetectorReport()
        dn = dc.create_node("dockerfile.j2")
        dn.register_detector(GolangVersionDetector())

        jn = dc.create_node("Jenkinsfile.j2")
        jn.register_detector(ImageRepoDetector())

        dcn = dc.create_node("docker-compose.yml.j2")
        dcn.register_detector(ImageRepoDetector())
        dc.generate_report()
