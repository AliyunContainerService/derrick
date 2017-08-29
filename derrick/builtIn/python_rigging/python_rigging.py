#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.rigging import Rigging

PLATFORM = "Python"


class PythonRiggle(Rigging):
    def detect(self, context):
        pass

    def compile(self, context):
        pass


# Every rigging should be able to run separately.
def main():
    pass


if __name__ == "__main__":
    main()
