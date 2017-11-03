import unittest

from derrick.detectors.image.golang import GolangVersionDetector


class TestGolangDetector(unittest.TestCase):
    def test_golang_detector(self):
        gr = GolangVersionDetector()
        version = gr.execute()
        print("golang version detected %s" % version)
        self.assertIsNotNone(version)
