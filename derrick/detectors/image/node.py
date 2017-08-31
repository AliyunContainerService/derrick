#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import subprocess

from derrick.core.detector import Detector
from derrick.core.logger import Logger

NODEJS_4 = "node:4"
NODEJS_6 = "node:6"
NODEJS_8 = "node:8"
NODEJS_LATEST = "node:latest"


class NodeVersionDetector(Detector):
    def execute(self):
        output = subprocess.check_output(["node",  "--version"], shell=False)
        version = self.get_most_relative_version(output)
        return version

    def get_most_relative_version(self, version):
        version_num = str(version)[1:]
        version_arr = version_num.split(".")

        detect_version = NODEJS_LATEST
        try:
            base_version = version_arr[0]
            if base_version == "4":
                detect_version = NODEJS_4
            if base_version == "6":
                detect_version = NODEJS_6
            if base_version == "8":
                detect_version = NODEJS_8
        except Exception as e:
            Logger.debug("system version is %s,error message is %s" % (version, e.message))
        return detect_version
