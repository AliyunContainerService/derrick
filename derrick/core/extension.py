#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ExtensionPoints(object):
    """
        ExtensionPoints will be used when you
        want to define a new entry to Derrick core
    """

    def __init__(self):
        self.ext_points = dict()

    # all() will return all ExtensionPoints
    def all(self):
        return self.ext_points

    # register(self,ext_point) will load the ExtensionPoint
    # and cache the instance to ExtensionPoints
    def register(self, ext_point):
        ext_name = ext_point.get_name()
        self.ext_points[ext_name] = ext_point.load()

    # try to load related some Extension Ponits
    def load(self):
        pass


class ExtensionPoint(object):
    # return the ExtensionPoint name
    def get_name(self):
        return self.name

    # load will be override by child class
    # You should always return self in the end
    def load(self):
        return self
