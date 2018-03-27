#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import re
import subprocess
import chardet
from derrick.core.detector import Detector
from derrick.core.logger import Logger

default_image = "openjdk"
default_version = "8"
regex = r"(?!\.)(\d+(\.\d+)+)([-.][A-Z]+)?(?![\d.])"


class JavaVersionDetector(Detector):
    def execute(self):
        print("Detecting Java version ...")
        version = default_version
        try:
            output = subprocess.check_output(["java", "-version"], shell=False, stderr=subprocess.STDOUT)
            version = JavaVersionDetector.get_most_relative_version(output.decode('utf-8'))
        except Exception as e:
            Logger.debug("Failed to detect Java version,because of %s" % e)
            Logger.debug("Use default Java version:%s instead ." % default_version)
        return {"version": version}

    @staticmethod
    def get_most_relative_version(version):
        version_bytes = str.encode(version)
        encode_type = chardet.detect(version_bytes)
        version_converted = version_bytes.decode(encode_type['encoding'])
        matches = re.search(regex, version_converted)
        detect_version = default_version
        if matches:
            version_arr = matches.group(1).split(".")
            if len(version_arr) > 1:
                # Java 7,8 version string is the format of "1.8.0_131"
                # Java 9 version string is like this: "9.0.1"
                if version_arr[0] == '1':
                    detect_version = version_arr[1]
                else:
                    detect_version = version_arr[0]

        return detect_version
