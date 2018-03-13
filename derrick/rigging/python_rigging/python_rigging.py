#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.detector_report import DetectorReport
from derrick.core.rigging import Rigging
from derrick.detectors.general.image_repo import ImageRepoDetector
from derrick.detectors.image.python import PythonVersionDetector
from derrick.detectors.platform.python.package_manager import PythonPakcageManager
from derrick.detectors.platform.python.framework import PythonFrameworkDetector
from derrick.detectors.general.derrick import DerrickDetector

PLATFORM = "Python"


class PythonRigging(Rigging):
    def detect(self, context):
        """
        requirements.txt or setup.py
        :param context:
        :return:
        """
        workspace = context.get("WORKSPACE")
        requirements_txt = os.path.join(workspace, "requirements.txt")
        setup_py = os.path.join(workspace, "setup.py")

        if os.path.exists(requirements_txt) is True or os.path.exists(setup_py) is True:
            return True, PLATFORM
        return False, None

    def compile(self, context):
        dr = DetectorReport()
        meta = dr.create_node("Meta")
        meta.register_detector(ImageRepoDetector())

        docker_node = dr.create_node("Dockerfile.j2")
        docker_node.register_detector(PythonVersionDetector())
        docker_node.register_detector(PythonPakcageManager())
        docker_node.register_detector(PythonFrameworkDetector())

        docker_compose_node = dr.create_node("docker-compose.yml.j2")
        docker_compose_node.register_detector(ImageRepoDetector())

        jenkins_file_node = dr.create_node("Jenkinsfile.j2")
        jenkins_file_node.register_detector(ImageRepoDetector())

        derrick_deployment_file_node = dr.create_node("kubernetes-deployment.yaml.j2")
        derrick_deployment_file_node.register_detector(ImageRepoDetector())
        derrick_deployment_file_node.register_detector(DerrickDetector())

        return dr.generate_report()
