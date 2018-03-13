#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.detector import Detector
from derrick.core.common import DERRICK_VERSION


def normalize_name(name):
    # return re.sub(r'[^a-z0-9]', '', name.lower())
    return name


def get_project_name():
    project = os.path.basename(os.path.abspath(""))
    if project:
        return normalize_name(project)

    return 'default'


class DerrickDetector(Detector):
    def execute(self, *args, **kwargs):
        return {
            "derrick_version": DERRICK_VERSION,
            "project_name": get_project_name()
        }
