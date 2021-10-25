import pymongo
from quizDomain import Quiz

class QuizDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["quiz"]
    
    def find_all(self):
        many_quiz = list(self._collection.find({}))
        many_quiz_objects = []
        for one_quiz in many_quiz:
            one_quiz_object = Quiz(
                class_id=one_quiz["_id"]["class_id"],
                course_id=one_quiz["_id"]["course_id"],
                lesson_id=one_quiz["_id"]["lesson_id"],
                title=one_quiz["title"],
                description=one_quiz["description"],
                time_limit=one_quiz["time_limit"],
                passing_percentage=one_quiz["passing_percentage"],
                is_final=one_quiz["is_final"]
            )
            many_quiz_objects.append(one_quiz_object)
        return many_quiz_objects
        

    def find_one(self, class_id,course_id,lesson_id ):
        #mongodb function - find_one
        #one_quiz is dictionary retrieved from monogodb 
        one_quiz = self._collection.find_one(dict({"_id.class_id": class_id, 
                                        "_id.course_id": course_id, 
                                        "_id.lesson_id": lesson_id }))

        quiz = Quiz( class_id=one_quiz["_id"]["class_id"],
                course_id=one_quiz["_id"]["course_id"],
                lesson_id=one_quiz["_id"]["lesson_id"],
                title=one_quiz["title"],
                description=one_quiz["description"],
                time_limit=one_quiz["time_limit"],
                passing_percentage=one_quiz["passing_percentage"],
                is_final=one_quiz["is_final"]
        )

        return quiz

    def insert_one(self, quiz):
        one_quiz = self._collection.insert_one(dict({
            "_id" : {
                "class_id" : quiz.get_class_id(),
                "course_id" :  quiz.get_course_id(),
                "lesson_id" :  quiz.get_lesson_id()
            },
            "title" : quiz.get_title(),
            "description" : quiz.get_description(),
            "time_limit" : quiz.get_time_limit(),
            "passing_percentage" :quiz.get_passing_percentage(),
            "is_final" : quiz.get_is_final()
        }))
        return "Inserted"


