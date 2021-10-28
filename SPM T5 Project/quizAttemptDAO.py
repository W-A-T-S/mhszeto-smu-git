import pymongo
from quizAttemptDomain import QuizAttempt

class QuizAttemptDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["quizAttempt"]
    
    def find_query(self, query):
            many_quiz_attempt = list(self._collection.find(dict(query)))
            many_quiz_attempt_objects = []
            for one_quiz_attempt in many_quiz_attempt:
                one_quiz_attempt_object = QuizAttempt(
                    quiz_attempt_id=one_quiz_attempt["_id"]["quiz_attempt_id"],
                    lesson_id=one_quiz_attempt["_id"]["lesson_id"], 
                    course_id=one_quiz_attempt["_id"]["course_id"], 
                    class_id=one_quiz_attempt["_id"]["class_id"], 
                    learner_username=one_quiz_attempt["_id"]["learner_username"], 
                    marks_awarded=one_quiz_attempt["marks_awarded"],
                    is_passed=one_quiz_attempt["is_passed"]
                )
                many_quiz_attempt_objects.append(one_quiz_attempt_object)
            return many_quiz_attempt_objects
    
    
    def find_one(self, quiz_attempt_id, course_id, class_id, lesson_id, learner_username):
        one_quiz_attempt = self._collection.find_one(dict({"_id.quiz_attempt_id": quiz_attempt_id,
                                        "_id.course_id": course_id, 
                                        "_id.class_id": class_id,
                                        "_id.lesson_id": lesson_id,
                                        "_id.learner_username": learner_username}))

        one_quiz_attempt_object = QuizAttempt( 
            quiz_attempt_id=one_quiz_attempt["_id"]["quiz_attempt_id"],
            lesson_id=one_quiz_attempt["_id"]["lesson_id"], 
            course_id=one_quiz_attempt["_id"]["course_id"], 
            class_id=one_quiz_attempt["_id"]["class_id"], 
            learner_username=one_quiz_attempt["_id"]["learner_username"], 
            marks_awarded=one_quiz_attempt["marks_awarded"],
            is_passed=one_quiz_attempt["is_passed"]
        )

        return one_quiz_attempt_object


    def insert_one(self, quiz_attempt):
        one_quiz_attempt = self._collection.insert_one(dict({
            "_id" : {
                "quiz_attempt_id": quiz_attempt.get_quiz_attempt_id(),
                "class_id" : quiz_attempt.get_class_id(),
                "course_id" :  quiz_attempt.get_course_id(),
                "lesson_id" :  quiz_attempt.get_lesson_id(),
                "learner_username":quiz_attempt.get_learner_username(),
            },
            "marks_awarded": quiz_attempt.get_marks_awarded(),
            "is_passed": quiz_attempt.get_is_passed()
     
        }))
        return "Inserted"

