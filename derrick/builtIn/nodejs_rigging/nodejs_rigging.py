#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.rigging import Rigging


PLATFORM = "NodeJs"

class NodejsRiggle(Rigging):
    def detect(self, context):
        """

        :param context:
        :return: handled(bool),platform(string)
        """
        workspace = context.get("workspace")
        package_json_file = os.path.join(workspace, "package.json")
        if os.path.exists(package_json_file) == True:
            return True, PLATFORM
        return False, None

    def compile(self, context):
        pass


# Every rigging should be able to run separately.
def main():
    pass


if __name__ == "__main__":
    main()
