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
                learner_username = one_assignment["_id"]["learner_username"],
                admin_username = one_assignment["_id"]["admin_username"],
                class_id = one_assignment["_id"]["class_id"],
                course_id = one_assignment["_id"]["course_id"],
                is_enrolment_approved = one_assignment["is_enrolment_approved"],
                is_completed = one_assignment["is_completed"]
            )
            many_assignments_list.append(one_assignment_object)
        return many_assignments_list

