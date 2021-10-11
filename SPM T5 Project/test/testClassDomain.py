import unittest
import sys
from datetime import datetime

sys.path.append("../../SPM T5 Project")
from classDomain import Class


class testClassDomain(unittest.TestCase):
    def setUp(self):
        self._class = Class(
            class_id="CL1",
            course_id="CR101",
            trainer_username="JohnnyDeppTheStar",
            trainer_name="Johnny Depp",
            admin_username="LarryTheAdmin",
            enrolment_open_date=datetime(2021, 9, 1),
            enrolment_close_date=datetime(2021, 9, 10),
            start_date_time=datetime(2021, 10, 1, 12, 00),
            end_date_time=datetime(2021, 12, 1, 12, 00),
            class_size=50,
            class_available_slots=25,
        )

    def tearDown(self):
        self._class = None

    def test_get_course_id(self):
        self.assertEqual(self._class.get_course_id(), "CR101")

    def test_get_class_id(self):
        self.assertEqual(self._class.get_class_id(), "CL1")

    def test_get_trainer_username(self):
        self.assertEqual(self._class.get_trainer_username(), "JohnnyDeppTheStar")

    def test_get_trainer_name(self):
        self.assertEqual(self._class.get_trainer_name(), "Johnny Depp")

    def test_get_admin_username(self):
        self.assertEqual(self._class.get_admin_username(), "LarryTheAdmin")

    def test_get_enrolment_open_date(self):
        self.assertEqual(self._class.get_enrolment_open_date(), datetime(2021, 9, 1))

    def test_get_enrolment_close_date(self):
        self.assertEqual(self._class.get_enrolment_close_date(), datetime(2021, 9, 10))

    def test_get_start_date_time(self):
        self.assertEqual(
            self._class.get_start_date_time(), datetime(2021, 10, 1, 12, 00)
        )

    def test_get_end_date_time(self):
        self.assertEqual(self._class.get_end_date_time(), datetime(2021, 12, 1, 12, 00))

    def test_get_class_size(self):
        self.assertEqual(self._class.get_class_size(), 50)

    def test_get_class_available_slots(self):
        self.assertEqual(self._class.get_class_available_slots(), 25)
