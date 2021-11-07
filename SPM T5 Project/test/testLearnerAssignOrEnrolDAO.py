import unittest
from unittest.mock import MagicMock, patch
import sys
import pymongo
from datetime import datetime

sys.path.append("../../../SPM T5 Project/user")
from LearnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO

sys.path.append("../../../SPM T5 Project/user")
from LearnerAssignOrEnrolDomain import LearnerAssignOrEnrol


class testLearnerAssignOrEnrolDAO(unittest.TestCase):
    def setUp(self):
        self.LearnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
         
        self._sampleLearnerAssignOrEnrolList = [
            LearnerAssignOrEnrol(
                
                class_id="CL1",
                course_id="CR101",
                admin_username="LarryTheAdmin",
                learner_username= "JohnSmithTheMan",
                is_enrolment_approved= "false",
                is_completed= "false",
                is_enrolment_rejected="true"
            ),
            LearnerAssignOrEnrol(
                class_id="CL1",
                course_id="CR101",
                admin_username="LarryTheAdmin",
                learner_username= "Tommythetech",
                is_enrolment_approved= "true",
                is_completed= "false",
                is_enrolment_rejected="false"
            ),
        ]
        '''
        self._sampleLearnerAssignOrEnrol = LearnerAssignOrEnrol(
   
            class_id="CL1",
            course_id="CR101",
            admin_username="LarryTheAdmin",
            learner_username= "JohnSmithTheMan",
            is_enrolment_approved= "true",
            is_completed= "false",
            is_enrolment_rejected="true"

        )
        '''
        self._sampleLearnerAssignOrEnrolListDict = [ {
            "_id": {"course_id": "CR101", "class_id": "CL1", "admin_username":"LarryTheAdmin", "learner_username":"MaryTheAdmin"},
            "is_enrolment_approved" : "true",
            "is_completed" : "false",
            "is_enrolment_rejected":"false"
        },
        {
            "_id": {"course_id": "CR101", "class_id": "CL1", "admin_username":"LarryTheAdmin", "learner_username":"KKTheTech"},
            "is_enrolment_approved" : "false",
            "is_completed" : "false",
            "is_enrolment_rejected":"true"
        }

        ]

    def tearDown(self):
        self._LearnerAssignOrEnrolDAO = None


    def test_find_query(self):
        collection_mock = self._LearnerAssignOrEnrolDAO._collection
        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[self._sampleLearnerAssignOrEnrolDict],
        )
        result = self._LearnerAssignOrEnrolDAO.find_query(
            query={
                "is_enrolment_approved": "true",
            }
        )
        self.assertEqual(
            result[0].get_class_id(),
            self._sampleLearnerAssignOrEnrolList[0].get_class_id(),
        )
        self.assertEqual(
            result[0].get_course_id(),
            self._sampleLearnerAssignOrEnrolList[0].get_course_id(),
        )
        self.assertEqual(
            result[0].get_admin_username(),
            self._sampleLearnerAssignOrEnrolList[0].get_admin_username(),
        )
        self.assertEqual(
            result[0].get_learner_username(),
            self._sampleLearnerAssignOrEnrolList[0].get_learner_username(),
        )
        self.assertEqual(
            result[0].get_is_enrolment_approved(),
            self._sampleLearnerAssignOrEnrolList[0].get_is_enrolment_approved(),
        )
        self.assertEqual(
            result[0].get_is_completed(),
            self._sampleLearnerAssignOrEnrolList[0].get_is_completed(),
        )

    def test_update_one(self):
        collection_mock = self._LearnerAssignOrEnrolDAO._collection

        collection_mock.update_one = MagicMock(
            collection_mock,
            return_value={
                "acknowledged": True,
                "matched_count": 1.0,
                "modified_count": 1.0,
            },
        )

        result = self._LearnerAssignOrEnrolDAO.update_one(
            queryIdentifier={"_id": {"course_id": "CR101", "class_id": "CL1", "admin_username":"LarryTheAdmin", "learner_username":"JohnSmithTheMan"}},
            queryValues={
                "$set": {
                   "is_enrolment_approved": "false",
                   "is_enrolment_rejected":"false"
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
               
    def test_delete_one(self):
        mockresult = self.__LearnerAssignOrEnrolDAO._collection
        mockresult.find_one = MagicMock(mockresult, return_value = self.__sampleLearnerAssignOrEnrolList[0])
        mockresult = self._LearnerAssignOrEnrolDAO.delete_one(
            {
                "_id.class_id": "CL1",
                "_id.course_id": "CR101",
                "_id.learner_username": "JohnSmithTheMan",
            }
        )
        self.assertEqual(len(mockresult), 0)
        
    def test_no_assignorenrol_found(self):

        collection_mock = self.__LearnerAssignOrEnrolDAO._collection
        collection_mock.find = MagicMock(
            collection_mock,
            return_value=[],
        )
        result = self.__LearnerAssignOrEnrolDAO.find_all()
        self.assertEqual(len(result), 0)
  
if __name__ == "__main__":
    unittest.main()