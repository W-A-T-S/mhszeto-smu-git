import unittest
import sys

sys.path.append("../../SPM T5 Project")
from courseDomain import Course


class testCourseDomain(unittest.TestCase):
    def setUp(self):
        self._course = Course(
            course_id="CR101",
            title="Introduction to printers",
            description="In this course you will be learning more about printers",
            is_retired=False,
            admin_username="LarryTheAdmin",
        )

    def tearDown(self):
        self._course = None

    def test_get_course_id(self):
        self.assertEqual(self._course.get_course_id(), "CR101")

    def test_get_title(self):
        self.assertEqual(self._course.get_title(), "Introduction to printers")

    def test_get_description(self):
        self.assertEqual(
            self._course.get_description(),
            "In this course you will be learning more about printers",
        )

    def test_get_is_retired(self):
        self.assertEqual(self._course.get_is_retired(), False)

    def test_get_admin_username(self):
        self.assertEqual(self._course.get_admin_username(), "LarryTheAdmin")
