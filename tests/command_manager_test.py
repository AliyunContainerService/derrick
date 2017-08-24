import unittest
from derrick.core.command_manager import CommandManager


class CommandManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.cm = CommandManager()

    def tearDown(self):
        self.cm = None

    def test_default_commands_load(self):
        size = self.cm.all().size()
        print size
