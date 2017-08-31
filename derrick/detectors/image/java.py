#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import subprocess
import re

from derrick.core.detector import Detector
from derrick.core.logger import Logger

default_image = "openjdk"
default_version = "latest"
regex = r"(?!\.)(\d+(\.\d+)+)([-.][A-Z]+)?(?![\d.])"


class JavaVersionDetector(Detector):
    def execute(self):
        print("Detecting Java version ...")
        output = subprocess.check_output(["java",  "-version"], shell=False, stderr=subprocess.STDOUT)
        version = self.get_most_relative_version(output)
        return version

    def get_most_relative_version(self, version):
        matches = re.search(regex, version)
        detect_version = default_version
        if matches:
            version_arr = matches.group(1).split(".")
            if len(version_arr) > 1:
                detect_version = version_arr[1]
                 
        return detect_version
