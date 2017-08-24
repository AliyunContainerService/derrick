"""
    Derrick
"""

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

    def run(self):
        pass

    # when you need to load custom user's command
    def get_commands_manager(self):
        return self.cm

    def check_first_setup(self):
        pass
