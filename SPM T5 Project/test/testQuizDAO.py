#QuizDAO Unit Testing -Law Yong Wei
import unittest
from unittest.mock import MagicMock, patch
import sys
import pymongo
from datetime import datetime

sys.path.append("../../../SPM T5 Project")
from quizDAO import QuizDAO

sys.path.append("../../SPM T5 Project")
from quizDomain import Quiz


class testQuizDAO(unittest.TestCase):
    def setUp(self):
        self._quizDAO  = QuizDAO()
        self._sampleQuiz= Quiz(
            class_id="CL1",
            course_id="CR101",
            lesson_id="L1",
            title="What's Printer?",
            description="Testing your printer knowledge",
            time_limit="60",
            passing_percentage="80",
            is_final= "true"
           
        )

        self._sampleQuizDict = {
            "_id": {"course_id": "CR101", "class_id": "CL1", "lesson_id":"L1"},
            "title":"What's Printer?",
            "description":"Testing your printer knowledge",
            "time_limit":"60",
            "passing_percentage":"80",
            "is_final": "true"
        }



    def tearDown(self):
        self._quizDAO = None


    def test_find_all(self):
        collection_mock = self._quizDAO._collection
        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[self._sampleQuizDict],
        )
        result = self._quizDAO.find_all()

        self.assertEqual(
            result[0].get_class_id(),
            self._sampleQuiz.get_class_id(),
        )

        self.assertEqual(
            result[0].get_course_id(),
            self._sampleQuiz.get_course_id(),
        )

        self.assertEqual(
            result[0].get_lesson_id(),
            self._sampleQuiz.get_lesson_id(),
        )

        self.assertEqual(
            result[0].get_title(),
            self._sampleQuiz.get_title(),
        )

        self.assertEqual(
            result[0].get_description(),
            self._sampleQuiz.get_description(),
        )

        self.assertEqual(
            result[0].get_time_limit(),
            self._sampleQuiz.get_time_limit(),
        )

        self.assertEqual(
            result[0].get_passing_percentage(),
            self._sampleQuiz.get_passing_percentage(),
        )

        self.assertEqual(
            result[0].get_is_final(),
            self._sampleQuiz.get_is_final(),
        )


    def test_find_one(self):
        collection_mock = self._quizDAO._collection
        collection_mock.find_one = MagicMock(
            collection_mock, return_value=self._sampleQuizDict
        )

        result = self._quizDAO.find_one("CL1", "CR101","L1")

        
        self.assertEqual(
            result.get_class_id(),
            self._sampleQuiz.get_class_id(),
        )

        self.assertEqual(
            result.get_course_id(),
            self._sampleQuiz.get_course_id(),
        )

        self.assertEqual(
            result.get_lesson_id(),
            self._sampleQuiz.get_lesson_id(),
        )

        self.assertEqual(
            result.get_title(),
            self._sampleQuiz.get_title(),
        )

        self.assertEqual(
            result.get_description(),
            self._sampleQuiz.get_description(),
        )

        self.assertEqual(
            result.get_time_limit(),
            self._sampleQuiz.get_time_limit(),
        )

        self.assertEqual(
            result.get_passing_percentage(),
            self._sampleQuiz.get_passing_percentage(),
        )

        self.assertEqual(
            result.get_is_final(),
            self._sampleQuiz.get_is_final(),
        )
    
    def test_no_quiz_found(self):
        mockQuiz = self._quizDAO._collection
        mockQuiz.find = MagicMock(
            mockQuiz, return_value=[]
        )
        quizResult = self._quizDAO.find_all()
        self.assertEqual(len(quizResult), 0)


  
if __name__ == "__main__":
    unittest.main()