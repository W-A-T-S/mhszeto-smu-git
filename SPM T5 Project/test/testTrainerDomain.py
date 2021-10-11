import unittest
import sys

sys.path.append("../../SPM T5 Project")
from trainerDomain import Trainer


class testTrainerDomain(unittest.TestCase):
    def setUp(self):
        self._trainer = Trainer(
            username="JaneTheEngineer",
            name="Jane Doe",
            current_designation="Senior Engineer",
        )

    def tearDown(self):
        self._trainer = None

    def test_get_username(self):
        self.assertEqual(self._trainer.get_username(), "JaneTheEngineer")

    def test_get_name(self):
        self.assertEqual(self._trainer.get_name(), "Jane Doe")

    def test_get_current_designation(self):
        self.assertEqual(self._trainer.get_current_designation(), "Senior Engineer")
