import pymongo
from trainerDomain import Trainer


class TrainerDAO:
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
        many_trainer = list(self._collection.find(dict({"is_trainer": True})))
        many_trainer_objects = []
        for one_trainer in many_trainer:
            one_course_object = Trainer(
                username=one_trainer["_id"]["username"],
                name=one_trainer["name"],
                current_designation=one_trainer["current_designation"],
            )
            many_trainer_objects.append(one_course_object)
        return many_trainer_objects
