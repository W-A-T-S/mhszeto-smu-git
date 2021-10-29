import pymongo
from lessonDomain import Lesson

class LessonDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["lesson"]

    def find_query(self, query):
        many_lesson = list(self._collection.find(dict(query)))
        many_lesson_objects = []
        for one_lesson in many_lesson:
            one_lesson_object = Lesson(
                
                lesson_id=one_lesson["_id"]["lesson_id"], 
                class_id=one_lesson["_id"]["class_id"], 
                course_id=one_lesson["_id"]["course_id"], 

                title=one_lesson["title"], 
                description=one_lesson["description"],
            )
            many_lesson_objects.append(one_lesson_object)
        return many_lesson_objects


    def find_one(self, lesson_id, class_id, course_id, ):
        one_lesson = self._collection.find_one(dict({"_id.class_id": class_id, 
                                        "_id.course_id": course_id, 
                                        "_id.lesson_id": lesson_id,
                                        "_id.lesson_id": lesson_id }))
        one_lesson_object = Lesson(
            lesson_id=one_lesson["_id"]["lesson_id"], 
            class_id=one_lesson["_id"]["class_id"], 
            course_id=one_lesson["_id"]["course_id"], 
            title=one_lesson["title"], 
            description=one_lesson["description"],
        )

        return one_lesson_object

