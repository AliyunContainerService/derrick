#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.rigging import Rigging

PLATFORM = "NodeJs"


class NodejsRigging(Rigging):
    def detect(self, context):
        """
        :param context:
        :return: handled(bool),platform(string)
        """
        workspace = context.get("WORKSPACE")
        package_json_file = os.path.join(workspace, "package.json")
        if os.path.exists(package_json_file) == True:
            return True, PLATFORM
        return False, None

    def compile(self, context):
        return {"Dockerfile.j2": dict()}
