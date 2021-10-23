import unittest
from unittest.mock import MagicMock
import sys

sys.path.append("../../../SPM T5 Project/")
from trainerDAO import TrainerDAO

sys.path.append("../../../SPM T5 Project/")
from trainerDomain import Trainer


class TestTrainerDAO(unittest.TestCase):
    def setUp(self):
        self.__trainerDAO = TrainerDAO()

        self.__sampleTrainerList = [
            Trainer(
                username="JaneTheEngineer",
                name="Jane Smith",
                current_designation="Senior Engineer",
            ),
            Trainer(
                username="BobTheCoolGuy",
                name="Bob Builder",
                current_designation="Senior Engineer",
            ),
        ]

        self.__sampleTrainerListDict = [
            {
                "_id": {"username": "JaneTheEnginee"},
                "name": "Jane Smith",
                "current_designation": "Senior Engineer",
                "is_trainer": True,
                "is_admin": False,
            },
            {
                "_id": {"username": "BobTheCoolGuy"},
                "name": "Bob Builder",
                "current_designation": "Senior Engineer",
                "is_trainer": True,
                "is_admin": False,
            },
        ]

    def tearDown(self):
        self.__trainerDAO = None

    def test_find_all_no_trainer_returned(self):
        collection_mock = self.__trainerDAO._collection

        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[],
        )

        result = self.__trainerDAO.find_all()

        self.assertEqual(len(result), 0)

    def test_find_all_one_trainer_returned(self):
        collection_mock = self.__trainerDAO._collection

        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[self.__sampleTrainerListDict[0]],
        )

        result = self.__trainerDAO.find_all()

        self.assertEqual(len(result), 1)

        self.assertEqual(
            result[0].get_username(),
            self.__sampleTrainerList[0].get_username(),
        )

        self.assertEqual(
            result[0].get_name(),
            self.__sampleTrainerList[0].get_name(),
        )

        self.assertEqual(
            result[0].get_current_designation(),
            self.__sampleTrainerList[0].get_current_designation(),
        )

    def test_find_all_multiple_trainer_returned(self):
        collection_mock = self.__trainerDAO._collection

        collection_mock.find = MagicMock(
            collection_mock,
            return_value=self.__sampleTrainerListDict,
        )

        result = self.__trainerDAO.find_all()

        self.assertEqual(len(result), 2)

        for idx, trainer in enumerate(result):
            self.assertEqual(
                trainer.get_username(),
                self.__sampleTrainerList[idx].get_username(),
            )

            self.assertEqual(
                trainer.get_name(),
                self.__sampleTrainerList[idx].get_name(),
            )

            self.assertEqual(
                trainer.get_current_designation(),
                self.__sampleTrainerList[idx].get_current_designation(),
            )
