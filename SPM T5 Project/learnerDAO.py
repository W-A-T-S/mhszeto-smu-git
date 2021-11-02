import pymongo
from learnerDomain import Learner


class LearnerDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["learner"]

    def find_all(self):
        many_learner = list(
            self._collection.find(dict({"is_trainer": False, "is_admin": False}))
        )
        many_learner_objects = []
        for one_learner in many_learner:
            one_learner_object = Learner(
                username=one_learner["_id"]["username"],
                name=one_learner["name"],
                current_designation=one_learner["current_designation"],
            )
            many_learner_objects.append(one_learner_object)
        return many_learner_objects

    def find_one(self, learner_username):
        # mongodb function - find_one
        # one_learner is dictionary retrieved from monogodb
        one_learner = self._collection.find_one(
            dict(
                {
                    "is_trainer": False,
                    "is_admin": False,
                    "_id.username": learner_username,
                }
            )
        )

        learner = Learner(
            username=one_learner["_id"]["username"],
            name=one_learner["name"],
            current_designation=one_learner["current_designation"],
        )

        return learner

    def update_one(self, queryIdentifier, queryValues):
        res = self._collection.update_one(queryIdentifier, queryValues)
        return res
