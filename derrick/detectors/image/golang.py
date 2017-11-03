#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import subprocess

from derrick.core.detector import Detector
from derrick.core.logger import Logger

GOLANG_1_8 = "1.8"
GOLANG_1_9 = "1.9"
GOLANG_1_7 = "1.7"

DEFAULT_VERSION = GOLANG_1_8


class GolangVersionDetector(Detector):
    def execute(self, *args, **kwargs):
        Logger.info("Detecting Golang version ...")
        version = DEFAULT_VERSION
        try:
            output = subprocess.check_output(["go", "version"], shell=False, stderr=subprocess.STDOUT)
            version = GolangVersionDetector.get_most_relative_version(output)
        except Exception as e:
            Logger.debug("Failed to detect Golang version,because of %s" % e)
            Logger.debug("Use default Golang version:%s instead ." % DEFAULT_VERSION)
        return {"version": version}

    @staticmethod
    def get_most_relative_version(output):
        versions = [GOLANG_1_7, GOLANG_1_8, GOLANG_1_9]
        version = filter(lambda x: "go" + x in output, versions)
        if len(version) == 0:
            return DEFAULT_VERSION
        return version[0]
