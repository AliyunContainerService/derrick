#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command


class Init(Command):
    # implement the interface
    def execute(self):
        print("Init derrick")

    # implement the interface
    def get_help_desc(self):
        return "derrick init [<rigging-name>]"
