#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from derrick.core.detector_report import DetectorReport
from derrick.core.rigging import Rigging
from derrick.detectors.general.image_repo import ImageRepoDetector
from derrick.detectors.image.java import JavaVersionDetector
from derrick.detectors.general.derrick import DerrickDetector

RUNTIME = "Maven"


class MavenRigging(Rigging):
    def detect(self, context):
        """
        :param context:
        :return: handled(bool),platform(string)
        """
        workspace = context.get("WORKSPACE")
        package_json_file = os.path.join(workspace, "pom.xml")
        if os.path.exists(package_json_file) is True:
            return True, RUNTIME
        return False, None

    def compile(self, context):
        dr = DetectorReport()
        meta = dr.create_node("Meta")
        meta.register_detector(ImageRepoDetector())

        docker_node = dr.create_node("Dockerfile.j2")
        docker_node.register_detector(JavaVersionDetector())

        docker_compose_node = dr.create_node("docker-compose.yml.j2")
        docker_compose_node.register_detector(ImageRepoDetector())

        jenkins_file_node = dr.create_node("Jenkinsfile.j2")
        jenkins_file_node.register_detector(ImageRepoDetector())

        derrick_deployment_file_node = dr.create_node("kubernetes-deployment.yaml.j2")
        derrick_deployment_file_node.register_detector(ImageRepoDetector())
        derrick_deployment_file_node.register_detector(DerrickDetector())
        return dr.generate_report()
