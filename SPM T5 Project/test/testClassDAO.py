import unittest
from unittest.mock import MagicMock, patch
import sys
import pymongo
from datetime import datetime

sys.path.append("../../SPM T5 Project")
from classDAO import ClassDAO

sys.path.append("../../SPM T5 Project")
from classDomain import Class


class testClassDOA(unittest.TestCase):
    def setUp(self):
        self._classDAO = ClassDAO()
        self._sampleClass = Class(
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
        self._sampleClassDict = {
            "_id": {"course_id": "CR101", "class_id": "CL1"},
            "trainer_name": "Johnny Depp",
            "trainer_username": "JohnnyDeppTheStar",
            "admin_username": "LarryTheAdmin",
            "enrolment_open_date": datetime(2021, 9, 1),
            "enrolment_close_date": datetime(2021, 9, 10),
            "start_date_time": datetime(2021, 10, 1, 12, 00),
            "end_date_time": datetime(2021, 12, 1, 12, 00),
            "class_size": 50,
            "class_available_slots": 25,
        }

    def tearDown(self):
        self._classDAO = None

    def test_find_all(self):
        collection_mock = self._classDAO._collection
        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[self._sampleClassDict],
        )
        result = self._classDAO.find_all()

        self.assertEqual(
            result[0].get_class_id(),
            self._sampleClass.get_class_id(),
        )

        self.assertEqual(
            result[0].get_course_id(),
            self._sampleClass.get_course_id(),
        )

        self.assertEqual(
            result[0].get_trainer_name(),
            self._sampleClass.get_trainer_name(),
        )

        self.assertEqual(
            result[0].get_trainer_username(),
            self._sampleClass.get_trainer_username(),
        )

        self.assertEqual(
            result[0].get_admin_username(),
            self._sampleClass.get_admin_username(),
        )

        self.assertEqual(
            result[0].get_enrolment_open_date(),
            self._sampleClass.get_enrolment_open_date(),
        )

        self.assertEqual(
            result[0].get_enrolment_close_date(),
            self._sampleClass.get_enrolment_close_date(),
        )

        self.assertEqual(
            result[0].get_start_date_time(),
            self._sampleClass.get_start_date_time(),
        )

        self.assertEqual(
            result[0].get_end_date_time(),
            self._sampleClass.get_end_date_time(),
        )

        self.assertEqual(
            result[0].get_class_size(),
            self._sampleClass.get_class_size(),
        )

    def test_find_one(self):
        collection_mock = self._classDAO._collection
        collection_mock.find_one = MagicMock(
            collection_mock, return_value=self._sampleClassDict
        )

        result = self._classDAO.find_one("CL1", "CR101")

        self.assertEqual(
            result.get_class_id(),
            self._sampleClass.get_class_id(),
        )

        self.assertEqual(
            result.get_course_id(),
            self._sampleClass.get_course_id(),
        )

        self.assertEqual(
            result.get_trainer_name(),
            self._sampleClass.get_trainer_name(),
        )

        self.assertEqual(
            result.get_trainer_username(),
            self._sampleClass.get_trainer_username(),
        )

        self.assertEqual(
            result.get_admin_username(),
            self._sampleClass.get_admin_username(),
        )

        self.assertEqual(
            result.get_enrolment_open_date(),
            self._sampleClass.get_enrolment_open_date(),
        )

        self.assertEqual(
            result.get_enrolment_close_date(),
            self._sampleClass.get_enrolment_close_date(),
        )

        self.assertEqual(
            result.get_start_date_time(),
            self._sampleClass.get_start_date_time(),
        )

        self.assertEqual(
            result.get_end_date_time(),
            self._sampleClass.get_end_date_time(),
        )

        self.assertEqual(
            result.get_class_size(),
            self._sampleClass.get_class_size(),
        )

    def test_find_query(self):
        collection_mock = self._classDAO._collection
        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[self._sampleClassDict],
        )
        result = self._classDAO.find_query(
            query={
                "I am a": "fake query",
            }
        )

        self.assertEqual(
            result[0].get_class_id(),
            self._sampleClass.get_class_id(),
        )

        self.assertEqual(
            result[0].get_course_id(),
            self._sampleClass.get_course_id(),
        )

        self.assertEqual(
            result[0].get_trainer_name(),
            self._sampleClass.get_trainer_name(),
        )

        self.assertEqual(
            result[0].get_trainer_username(),
            self._sampleClass.get_trainer_username(),
        )

        self.assertEqual(
            result[0].get_admin_username(),
            self._sampleClass.get_admin_username(),
        )

        self.assertEqual(
            result[0].get_enrolment_open_date(),
            self._sampleClass.get_enrolment_open_date(),
        )

        self.assertEqual(
            result[0].get_enrolment_close_date(),
            self._sampleClass.get_enrolment_close_date(),
        )

        self.assertEqual(
            result[0].get_start_date_time(),
            self._sampleClass.get_start_date_time(),
        )

        self.assertEqual(
            result[0].get_end_date_time(),
            self._sampleClass.get_end_date_time(),
        )

        self.assertEqual(
            result[0].get_class_size(),
            self._sampleClass.get_class_size(),
        )

    def test_update_one(self):
        collection_mock = self._classDAO._collection

        collection_mock.update_one = MagicMock(
            collection_mock,
            return_value={
                "acknowledged": True,
                "matched_count": 1.0,
                "modified_count": 1.0,
            },
        )

        result = self._classDAO.update_one(
            queryIdentifier={"_id": {"course_id": "CR101", "class_id": "CL1"}},
            queryValues={
                "$set": {
                    "trainer_name": "Jane Done",
                    "trainer_username": "JaneTheEngineer",
                }
            },
        )

        self.assertEqual(
            result["acknowledged"],
            True,
        )

        self.assertEqual(
            result["matched_count"],
            1.0,
        )

        self.assertEqual(
            result["modified_count"],
            1.0,
        )
