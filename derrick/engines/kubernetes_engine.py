#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
from derrick.core.engine import Engine
from derrick.core.common import *
from derrick.core.logger import Logger
from derrick.core.recorder import ApplicationRecorder


class KubernetesEngine(Engine):
    def up(self, *args, **kwargs):
        need_build = True
        image_with_tag = ApplicationRecorder().get_record("image_with_tag")
        if image_with_tag is None:
            Logger.warnf("Failed to find your docker image, You should build it by your self.")
            need_build = False
        if is_windows() is True:
            try:
                import win32api
                if need_build is True:
                    win32api.WinExec('docker build -t %s .' % image_with_tag)
                win32api.WinExec('kubectl apply -f kubernetes-deployment.yaml')
            except Exception as e:
                Logger.error("Can not start your application.Have you installed kubelet in path?")
            return
        status = os.system("docker build -t %s ." % image_with_tag)
        if status != 0:
            Logger.info("Failed to build docker image, Have you installed docker in path?")
            sys.exit(-1)
        status = os.system("docker push %s" % image_with_tag)
        if status != 0:
            Logger.info("Failed to push docker image %s" % image_with_tag)
            sys.exit(-1)
        status = os.system("kubectl apply -f kubernetes-deployment.yaml")
        if status == 0:
            Logger.info("Your application has been up to running! You can run `kubectl get svc` to get exposed ports.")
        else:
            Logger.error("Can not start your application.Have you installed kubelet in path?")
