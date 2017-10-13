#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import subprocess

from derrick.core.detector import Detector
from derrick.core.logger import Logger

NODEJS_4 = "4"
NODEJS_6 = "6"
NODEJS_8 = "8"


class NodeVersionDetector(Detector):
    def execute(self):
        try:
            output = subprocess.check_output(["node", "--version"], shell=False)
            Logger.debug("NodeJs version detected is %s" % output)
            version = NodeVersionDetector.get_most_relative_version(output)
        except:
            version = NODEJS_8

        return {"version": version}

    @staticmethod
    def get_most_relative_version(version):
        version_num = str(version)[1:]
        version_arr = version_num.split(".")

        detect_version = NODEJS_8
        try:
            base_version = version_arr[0]
            if base_version == "4":
                detect_version = NODEJS_4
            if base_version == "6":
                detect_version = NODEJS_6
            if base_version == "8":
                detect_version = NODEJS_8
        except Exception as e:
            Logger.debug("system version is %s,error message is %s" % (version, e))
        return detect_version
