#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import subprocess

from derrick.core.detector import Detector
from derrick.core.logger import Logger

PYTHON_2 = "2.7"
PYTHON_3 = "3.6"


class PythonVersionDetector(Detector):
    def execute(self, *args, **kwargs):
        try:
            output = subprocess.check_output(["python", "--version"], shell=False)
            Logger.debug("NodeJs version detected is %s" % output)
            version = PythonVersionDetector.get_most_relative_version(output)
        except:
            version = PYTHON_2
        return {"version": version}

    @staticmethod
    def get_most_relative_version(version):
        try:
            version_section = version.split(" ")[1]
            if version_section.startswith("2") is True:
                return PYTHON_2
            if version_section.startswith("3") is True:
                return PYTHON_3
        except Exception as e:
            Logger.debug("Failed to detect Python version(%s) and use default Python version" % version)
            Logger.debug("Stacktrace is %s" % e)

        return PYTHON_2
