#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class RiggingDetectInfo(dict):
    def __init__(self, rigging_name, platform, image_with_tag):
        self.__setitem__("rigging_name", rigging_name)
        self.__setitem__("platform", platform)
        self.__setitem__("image_with_tag", image_with_tag)
