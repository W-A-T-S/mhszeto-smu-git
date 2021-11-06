#Test Cases done by: Hajarah Parveen
#CRUD of Learners

import unittest
import sys
from unittest.mock import MagicMock
from learnerDAO import learnerDAO
from learnerDomain import Learner

class TestLearnerDAO(unittest.TestCase):
    def setUp(self):
        self.__learnerDAO = learnerDAO()

        self.__sampleLearnerList = [
            Learner(
                username="JaneTheEngineer",
                name="Jane Doe",
                current_designation="Year 1",
            ),
            Learner(
                username="BobTheCoolGuy",
                name="Bob Builder",
                current_designation="Year 5",
            ),
        ]

        self.__sampleLearnerListDict = [
            {
                "_id": {"username": "JaneTheEngineer"},
                "name": "Jane Doe",
                "current_designation": "Year 1",
                "is_learner": True,
                "is_admin": False,
            },
            {
                "_id": {"username": "BobTheCoolGuy"},
                "name": "Bob Builder",
                "current_designation": "Year 5",
                "is_learner": True,
                "is_admin": False,
            },
        ]

def tearDown(self):
        self.__learnerDAO = None

def test_find_all_no_learner_returned(self):
        collection_mock = self.__learnerDAO._collection

        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[],
        )

        result = self.__learnerDAO.find_all()

        self.assertEqual(len(result), 0)

def test_find_all_one_learner_returned(self):
        collection_mock = self.__learnerDAO._collection

        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[self.__sampleLearnerListDict[0]],
        )

        result = self.__learnerDAO.find_all()

        self.assertEqual(len(result), 1)

        self.assertEqual(
            result[0].get_username(),
            self.__sampleLearnerList[0].get_username(),
        )

        self.assertEqual(
            result[0].get_name(),
            self.__sampleLearnerList[0].get_name(),
        )

        self.assertEqual(
            result[0].get_current_designation(),
            self.__sampleLearnerList[0].get_current_designation(),
        )

def test_find_all_learner_returned(self):
        collection_mock = self.__learnerDAO._collection

        collection_mock.find = MagicMock(
            collection_mock,
            return_value=self.__sampleLearnerListDict,
        )

        result = self.__learnerDAO.find_all()

        self.assertEqual(len(result), 2)

        for idx, learner in enumerate(result):
            self.assertEqual(
                learner.get_username(),
                self.__sampleLearnerList[idx].get_username(),
            )

            self.assertEqual(
                learner.get_name(),
                self.__sampleLearnerList[idx].get_name(),
            )

            self.assertEqual(
                learner.get_current_designation(),
                self.__sampleLearnerList[idx].get_current_designation(),
            )

if __name__ == "__main__":
    unittest.main()
