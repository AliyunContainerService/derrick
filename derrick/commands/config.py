#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command


class Config(Command):
    """
    Config command is to switch some mode in derrick
    almost every develop would like to use just one
    orchestration: swarm,kubernetes or something else.

    and it is the same when meets ci/cd pipeline.

    So Derrick should have a command to config the switch
    """

    def execute(self, context):
        pass

        # docopt will combine all the desc to one single help

    def get_help_desc(self):
        return "derrick config"
