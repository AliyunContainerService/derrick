#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from derrick.core.command import Command
from whaaaaat import style_from_dict, Token, prompt
from derrick.core.derrick import Derrick
from derrick.core.logger import Logger


class Config(Command):
    """
    Config command is to switch some mode in derrick
    almost every develop would like to use just one
    orchestration: swarm,kubernetes or something else.

    and it is the same when meets ci/cd pipeline.

    So Derrick should have a command to config the switch
    """

    def execute(self, context):
        questions = [
            {
                'type': 'list',
                'name': 'engine',
                'message': 'Which Orchestration Engine would you like to choose?',
                'choices': ["Kubernetes", "Swarm"]
            }
        ]
        style = style_from_dict({
            Token.Selected: '#00FFFF bold',
        })
        answers = prompt(questions, style=style)
        recorder = Derrick().get_recorder()
        try:
            recorder.record(answers)
        except Exception as e:
            Logger.error("Failed to record config, Because of %s"%e)

    def get_help_desc(self):
        return "derrick config"
