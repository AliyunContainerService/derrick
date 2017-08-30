#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command
import derrick.core.logger as log


class Build(Command):
    """
    Docker 17.05.0-ce support multi-stage build
    We recommend you to use latest version Docker CE
    Multi-stage build is very useful for Java or
    other languages that need to be compiled.

    If you can't use the latest version of Docker
    You can also build and package code with the
    language specific build tool and mount the
    artifacts with docker volume.
    """

    # implement the interface
    def execute(self, context):
        log.info("Start to build application.")
        pass

    # implement the interface
    def get_help_desc(self):
        return "derrick build"

