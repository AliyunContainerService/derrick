#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import subprocess

from derrick.core.detector import Detector
from derrick.core.logger import Logger

PHP_5 = "5"
PHP_7 = "7"

DEFAULT_VERSION = PHP_7


class PhpVersionDetector(Detector):
    def execute(self, *args, **kwargs):
        Logger.info("Detecting PHP version ...")
        version = DEFAULT_VERSION
        try:
            output = subprocess.check_output(["php", "-version"], shell=False, stderr=subprocess.STDOUT)
            version = PhpVersionDetector.get_most_relative_version(output)
        except Exception as e:
            Logger.debug("Failed to detect PHP version,because of %s" % e)
            Logger.debug("Use default PHP version:%s instead ." % DEFAULT_VERSION)
        return {"version": version}

    @staticmethod
    def get_most_relative_version(output):
        versions = [PHP_5, PHP_7]
        version = filter(lambda x: ("PHP " + x) in output, versions)
        if len(version) == 0:
            return DEFAULT_VERSION
        return version[0]
