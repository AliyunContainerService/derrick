#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
from whaaaaat import prompt

from derrick.core.detector import Detector
from derrick.core.logger import Logger


class ImageRepoDetector(Detector):
    def execute(self, *args, **kwargs):
        try:
            questions = [
                {
                    'type': 'input',
                    'name': 'image_with_tag',
                    'message': 'Please input image name with tag (such as "registry.com/user/repo:tag"): ',
                }
            ]
            answers = prompt(questions)
            if len(answers.keys()) is 0:
                sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            Logger.warn("Failed to detect image repo. Windows console don't support prompt action.")
            Logger.warn("Jenkinsfile and docker-compose.yml may not be generated completely.")
            answers = {"image_with_tag": "[IMAGE_WITH_TAG]"}
        return answers
