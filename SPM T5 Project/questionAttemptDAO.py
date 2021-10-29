import pymongo
from questionAttemptDomain import QuestionAttempt


class QuestionAttemptDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["questionAttempt"]

    def insert_many(self, many_question_attempt):
        for one_question_attempt in many_question_attempt:
            self._collection.insert_one(
                dict(
                    {
                        "_id": {
                            "question_id": one_question_attempt.get_question_id(),
                            "question_attempt_id": one_question_attempt.get_question_attempt_id(),
                            "quiz_attempt_id": one_question_attempt.get_quiz_attempt_id(),
                            "lesson_id": one_question_attempt.get_lesson_id(),
                            "class_id": one_question_attempt.get_class_id(),
                            "course_id": one_question_attempt.get_course_id(),
                            "learner_username": one_question_attempt.get_learner_username(),
                        },
                        "selected_option": one_question_attempt.get_selected_option(),
                        "is_correct": one_question_attempt.get_is_correct(),
                    }
                )
            )
        return

    def find_query(self, query):
        many_question_attempt = list(self._collection.find(query))
        many_question_attempt_obj = []
        for one_question_attempt in many_question_attempt:
            one_question_attempt_obj = QuestionAttempt(
                question_id=one_question_attempt["_id"]["question_id"],
                question_attempt_id=one_question_attempt["_id"]["question_attempt_id"],
                quiz_attempt_id=one_question_attempt["_id"]["question_attempt_id"],
                lesson_id=one_question_attempt["_id"]["lesson_id"],
                class_id=one_question_attempt["_id"]["class_id"],
                course_id=one_question_attempt["_id"]["course_id"],
                learner_username=one_question_attempt["_id"]["learner_username"],
                selected_option=one_question_attempt["selected_option"],
                is_correct=one_question_attempt["is_correct"],
            )
            many_question_attempt_obj.append(one_question_attempt_obj)
        return many_question_attempt_obj
