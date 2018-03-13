#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.engine import Engine
from derrick.core.common import *
from derrick.core.logger import Logger


class SwarmEngine(Engine):
    def up(self, *args, **kwargs):
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
