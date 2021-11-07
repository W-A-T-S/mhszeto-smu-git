import pymongo
from questionDomain import Question


class QuestionDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["question"]

    def find_all(self):
        many_question = list(self._collection.find({}))
        many_question_objects = []
        for one_question in many_question:
            one_question_object = Question(
                question_id=one_question["_id"]["question_id"],
                lesson_id=one_question["_id"]["lesson_id"],
                class_id=one_question["_id"]["class_id"],
                course_id=one_question["_id"]["course_id"],
                question=one_question["question"],
                options=one_question["options"],
                answer=one_question["answer"],
            )
            many_question_objects.append(one_question_object)
        return many_question_objects

    def find_all_question_in_quiz(self, class_id, course_id, lesson_id):
        many_question = list(
            self._collection.find(
                {
                    "_id.class_id": class_id,
                    "_id.course_id": course_id,
                    "_id.lesson_id": lesson_id,
                }
            )
        )
        many_question_objects = []
        for one_question in many_question:
            one_question_object = Question(
                question_id=one_question["_id"]["question_id"],
                lesson_id=one_question["_id"]["lesson_id"],
                class_id=one_question["_id"]["class_id"],
                course_id=one_question["_id"]["course_id"],
                question=one_question["question"],
                options=one_question["options"],
                answer=one_question["answer"],
            )
            many_question_objects.append(one_question_object)
        return many_question_objects

    def find_one(self, class_id, course_id, lesson_id):
     
        one_question = self._collection.find_one(
            dict(
                {
                    "_id.class_id": class_id,
                    "_id.course_id": course_id,
                    "_id.lesson_id": lesson_id,
                }
            )
        )

        question = Question(
            question_id=one_question["_id"]["question_id"],
            lesson_id=one_question["_id"]["lesson_id"],
            class_id=one_question["_id"]["class_id"],
            course_id=one_question["_id"]["course_id"],
            question=one_question["question"],
            options=one_question["options"],
            answer=one_question["answer"],
        )

        return question

    def insert_one(self, question):
        self._collection.insert_one(
            dict(
                {
                    "_id": {
                        "question_id": question.get_question_id(),
                        "class_id": question.get_class_id(),
                        "course_id": question.get_course_id(),
                        "lesson_id": question.get_lesson_id(),
                    },
                    "question": question.get_question(),
                    "options": question.get_options(),
                    "answer": question.get_answer(),
                }
            )
        )

        return
