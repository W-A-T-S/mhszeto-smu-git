import pymongo
from learnerAssignOrEnrolDomain import LearnerAssignOrEnrol


class LearnerAssignOrEnrolDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["learnerAssignOrEnrol"]

    def find_query(self, query):
        many_assignments = list(self._collection.find(dict(query)))
        many_assignments_list = []
        for one_assignment in many_assignments:
            one_assignment_object = LearnerAssignOrEnrol(
                learner_username=one_assignment["_id"]["learner_username"],
                admin_username=one_assignment["_id"]["admin_username"],
                class_id=one_assignment["_id"]["class_id"],
                course_id=one_assignment["_id"]["course_id"],
                is_enrolment_approved=one_assignment["is_enrolment_approved"],
                is_completed=one_assignment["is_completed"],
                is_enrolment_rejected=one_assignment["is_enrolment_rejected"],
            )
            many_assignments_list.append(one_assignment_object)
        return many_assignments_list

    def insert_one(self, one_assignment_obj):

        self._collection.insert_one(
            dict(
                {
                    "_id": {
                        "learner_username": one_assignment_obj.get_learner_username(),
                        "admin_username": one_assignment_obj.get_admin_username(),
                        "class_id": one_assignment_obj.get_class_id(),
                        "course_id": one_assignment_obj.get_course_id(),
                    },
                    "is_enrolment_approved": one_assignment_obj.get_is_enrolment_approved(),
                    "is_completed": one_assignment_obj.get_is_completed(),
                    "is_enrolment_rejected": one_assignment_obj.get_is_enrolment_rejected(),
                }
            )
        )

    def delete_one(self, class_id, course_id, learner_username):
        self._collection.delete_one(
            {
                "_id.class_id": class_id,
                "_id.course_id": course_id,
                "_id.learner_username": learner_username,
            }
        )

    def update_one(self, queryIdentifier, queryValues):
        res = self._collection.update_one(queryIdentifier, queryValues)
        return res
