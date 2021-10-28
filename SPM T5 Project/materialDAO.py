import pymongo
from materialDomain import Material

class MaterialDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["material"]

    def find_query(self, query):
        many_material = list(self._collection.find(dict(query)))
        many_material_objects = []
        for one_material in many_material:
            one_material_object = Material(
                material_id=one_material["_id"]["material_id"], 
                lesson_id=one_material["_id"]["lesson_id"], 
                course_id=one_material["_id"]["course_id"], 
                class_id=one_material["_id"]["class_id"], 
                title=one_material["title"], 
                description=one_material["description"],
                material_type=one_material["type"], 
                url=one_material["url"])
            many_material_objects.append(one_material_object)
        return many_material_objects


    def find_one(self, class_id, course_id, lesson_id, material_id):
        one_material = self._collection.find_one(dict({"_id.class_id": class_id, 
                                        "_id.course_id": course_id, 
                                        "_id.lesson_id": lesson_id,
                                        "_id.material_id": material_id }))
        one_material_object = Material(
            material_id=one_material["_id"]["material_id"], 
            lesson_id=one_material["_id"]["lesson_id"], 
            course_id=one_material["_id"]["course_id"], 
            class_id=one_material["_id"]["class_id"], 
            title=one_material["title"], 
            description=one_material["description"],
            material_type=one_material["type"],
            url=one_material["url"])

        return one_material_object

