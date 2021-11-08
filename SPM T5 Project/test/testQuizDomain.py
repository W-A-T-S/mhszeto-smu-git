#test quiz domain - Law Yong Wei
import unittest
import sys

sys.path.append("../../SPM T5 Project")
from quizDomain import Quiz


class testQuizDomain(unittest.TestCase):
    def setUp(self):
        self._quiz = Quiz(
            class_id="CL1",
            course_id="CR101",
            lesson_id="L1",
            title="All about printer",
            description="Testing your printer knowledge",
            time_limit="60",
            passing_percentage="80",
            is_final= "true"
        )

    def tearDown(self):
        self._quiz = None
    
    def test_get_class_id(self):
        self.assertEqual(self._quiz.get_class_id(), "CL1")

    def test_get_course_id(self):
        self.assertEqual(self._quiz.get_course_id(), "CR101")

    def test_get_lesson_id(self):
        self.assertEqual(self._quiz.get_lesson_id(), "L1")

    def test_get_title(self):
        self.assertEqual(self._quiz.get_title(), "All about printer")

    def test_get_description(self):
        self.assertEqual(self._quiz.get_description(), "Testing your printer knowledge")

    def test_get_time_limit(self):
        self.assertEqual(self._quiz.get_time_limit(), "60")

    def test_passing_percentage(self):
        self.assertEqual(self._quiz.get_passing_percentage(), "80")
   
    def test_get_is_final(self):
        self.assertEqual(self._quiz.get_is_final(), "true")

   