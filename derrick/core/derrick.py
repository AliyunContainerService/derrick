"""
    Derrick
"""
from __future__ import absolute_import, division, print_function

from derrick.core.command_manager import CommandManager


class Derrick(object):
    def __init__(self):
        self.cm = CommandManager()

    # derrick lifecycle

    def pre_load(self):
        pass

    def load(self):
        self.pre_load()
        pass

    @staticmethod
    def run():
        pass

    # when you need to load custom user's command
    def get_commands_manager(self):
        return self.cm

    def check_first_setup(self):
        pass
