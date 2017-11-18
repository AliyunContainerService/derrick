#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command
from derrick.core.common import *
from derrick.core.logger import Logger


class Up(Command):
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
        if check_application_first_setup() is True:
            Logger.info("Your application haven't been initialized,you can run `derrick init`.")
            return

        if check_dockerfile_exists() is False:
            Logger.info("Dockerfile is not exists, Maybe you can rerun `derrick init` to resolve it.")
            return
        if is_windows() is True:
            try:
                import win32api
                win32api.WinExec('docker-compose up --build -d ')
            except Exception as e:
                Logger.error("Can not start your application.Have you installed docker-compose in path?")
            return
        status = os.system("/bin/bash -i -c 'docker-compose up --build -d '")
        if status == 0:
            Logger.info("Your application has been up to running! You can run `docker ps` to get exposed ports.")
        else:
            Logger.error("Can not start your application.Have you installed docker-compose in path?")

    # implement the interface
    def get_help_desc(self):
        return "derrick up"
