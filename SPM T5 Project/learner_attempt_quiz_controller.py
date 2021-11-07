from flask import Flask, render_template, request, jsonify, redirect
from courseDAO import CourseDAO
from classDAO import ClassDAO
from trainerDAO import TrainerDAO
from learnerDAO import LearnerDAO
from materialCheckDAO import MaterialCheckDAO
from quizAttemptDAO import QuizAttemptDAO
from quizAttemptDomain import QuizAttempt
from lessonDAO import LessonDAO
from materialDAO import MaterialDAO
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
from questionDAO import QuestionDAO
from quizDAO import QuizDAO
import json

app = Flask(__name__, template_folder="./Templates")


@app.route("/view_quiz/<string:class_id>/<string:course_id>/<string:lesson_id>")
def view_quiz(class_id, course_id, lesson_id):
    quizDao = QuizDAO()
    questionDAO = QuestionDAO()

    # class_id=one_quiz["_id"]["class_id"],
    #      course_id=one_quiz["_id"]["course_id"],
    #       lesson_id=one_quiz["_id"]["lesson_id"],
    #             title=one_quiz["title"],
    #             description=one_quiz["description"],
    #             time_limit=one_quiz["time_limit"],
    #             passing_percentage=one_quiz["passing_percentage"],
    #             is_final=one_quiz["is_final"]

    one_quiz = quizDao.find_one(
        course_id=course_id, class_id=class_id, lesson_id=lesson_id
    )
    all_questions = questionDAO.find_all_question_in_quiz(
        course_id=course_id, class_id=class_id, lesson_id=lesson_id
    )
    quiz_dict = {
        "class_id": class_id,
        "course_id": course_id,
        "lesson_id": lesson_id,
        "title": one_quiz.get_title(),
        "description": one_quiz.get_description(),
        "time_limit": one_quiz.get_time_limit(),
        "passing_percentage": one_quiz.get_passing_percentage(),
        "is_final": one_quiz.get_is_final(),
        "question_list": [],
    }

    for one_question in all_questions:
        quiz_dict["question_list"].append(
            {
                "question": one_question.get_question(),
                "choices": one_question.get_options(),
                "correctAnswer": one_question.get_answer(),
            }
        )

    return render_template("takequiz.html", quiz=json.dumps(quiz_dict))


@app.route("/view_quiz/<string:class_id>/<string:course_id>")
def view_final_quiz(class_id, course_id):
    quizDao = QuizDAO()
    questionDAO = QuestionDAO()

    one_quiz = quizDao.find_one(course_id=course_id, class_id=class_id, lesson_id=None)
    all_questions = questionDAO.find_all_question_in_quiz(
        course_id=course_id, class_id=class_id, lesson_id=None
    )
    quiz_dict = {
        "class_id": class_id,
        "course_id": course_id,
        "lesson_id": None,
        "title": one_quiz.get_title(),
        "description": one_quiz.get_description(),
        "time_limit": one_quiz.get_time_limit(),
        "passing_percentage": one_quiz.get_passing_percentage(),
        "is_final": one_quiz.get_is_final(),
        "question_list": [],
    }

    for one_question in all_questions:
        quiz_dict["question_list"].append(
            {
                "question": one_question.get_question(),
                "choices": one_question.get_options(),
                "correctAnswer": one_question.get_answer(),
            }
        )

    return render_template("learner_take_quiz.html", quiz=json.dumps(quiz_dict))


@app.route("/update_attempt", methods=["POST"])
def update_attempt():
    quizAttemptDAO = QuizAttemptDAO()
    one_quiz_attempt_obj = QuizAttempt(
        quiz_attempt_id=request.json["quiz_attempt_id"],
        lesson_id=request.json["lesson_id"],
        class_id=request.json["class_id"],
        course_id=request.json["course_id"],
        learner_username=request.json["learner_username"],
        marks_awarded=request.json["marks_awarded"],
        is_passed=request.json["is_passed"],
    )

    quizAttemptDAO.insert_one(one_quiz_attempt_obj)

    if request.json["lesson_id"] == None:
        learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
        update_learner_status_class_complete = learnerAssignOrEnrolDAO.update_one(
            queryIdentifier={
                "_id.course_id": request.json["course_id"],
                "_id.class_id": request.json["class_id"],
                "_id.learner_username": request.json["learner_username"],
            },
            queryValues={"$set": {"is_completed": True}},
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008, debug=True)
