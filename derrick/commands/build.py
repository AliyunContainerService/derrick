#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command
from derrick.core.common import *
from derrick.core.logger import Logger


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
        if check_application_first_setup() is True:
            Logger.info("Your application haven't been initialized,you can run `derrick init`.")
            return

        if check_dockerfile_exists() is False:
            Logger.info("Dockerfile is not exists, Maybe you can rerun `derrick init` to resolve it.")
            return

        # TODO Maybe a timestamp is better
        repo_name = os.path.basename(get_workspace()).lower()
        repo_tag = "latest"
        status = os.system("/bin/bash -i -c 'docker build -t %s .'" % (repo_name + ":" + repo_tag))
        if status == 0:
            Logger.info("Build %s:%s successfully.You can execute `docker run` to run this image."
                        % (repo_name, repo_tag))

    # implement the interface
    def get_help_desc(self):
        return "derrick build"
