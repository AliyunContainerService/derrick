#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.detector import Detector
from whaaaaat import prompt

class ImageRepoDetector(Detector):
    def execute(self, *args, **kwargs):
        questions = [
            {
                'type': 'input',
                'name': 'image_with_tag',
                'message': 'What\'s your image repo ',
            }
        ]
        answers = prompt(questions)
        return answers

