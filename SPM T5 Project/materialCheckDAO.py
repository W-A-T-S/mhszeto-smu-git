import pymongo
from materialCheckDomain import MaterialCheck

class MaterialCheckDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["materialCheck"]

    def find_query(self, query):
            many_material_check = list(self._collection.find(dict(query)))
            many_material_check_objects = []
            for one_material_check in many_material_check:
                one_material_check_object = MaterialCheck(
                    material_id=one_material_check["_id"]["material_id"], 
                    lesson_id=one_material_check["_id"]["lesson_id"], 
                    course_id=one_material_check["_id"]["course_id"], 
                    class_id=one_material_check["_id"]["class_id"], 
                    learner_username=one_material_check["_id"]["learner_username"], 
                    is_material_completed=one_material_check["is_material_completed"]
                )
                many_material_check_objects.append(one_material_check_object)
            return many_material_check_objects


    def find_one(self, class_id, course_id, lesson_id, material_id, learner_username):
        one_material_check = self._collection.find_one(dict({"_id.class_id": class_id, 
                                        "_id.course_id": course_id, 
                                        "_id.lesson_id": lesson_id,
                                        "_id.material_id": material_id,
                                        "_id.learner_username": learner_username}))
        one_material_check_object = MaterialCheck(
            material_id=one_material_check["_id"]["material_id"], 
            lesson_id=one_material_check["_id"]["lesson_id"], 
            course_id=one_material_check["_id"]["course_id"], 
            class_id=one_material_check["_id"]["class_id"], 
            learner_username=one_material_check["_id"]["learner_username"], 
            is_material_completed=one_material_check["is_material_completed"]
        )
        return one_material_check_object

    def update_one(self, queryIdentifier, queryValues):
        self._collection.update_one(queryIdentifier, queryValues)

        return "updated"

