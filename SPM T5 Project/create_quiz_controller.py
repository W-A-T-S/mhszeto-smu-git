from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from functools import wraps
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from os import environ
from quizDAO import QuizDAO
from quizDomain import Quiz
from questionDomain import Question
from questionDAO import QuestionDAO
import dateutil.parser

app = Flask(__name__)

# create new quiz
@app.route("/create_quiz", methods=["POST"])
def create_quiz():
    # try:
    # Quiz
    quizDAO = QuizDAO()
    passing_percentage=int(request.json["passing_percentage"])
    lesson_id=request.json["lesson_id"]
    if bool(int(request.json["is_final"])):
        lesson_id=None
    else: 
        passing_percentage=0

    one_quiz_object = Quiz(
        class_id=request.json["class_id"],
        course_id=request.json["course_id"],
        lesson_id=lesson_id,
        title=request.json["title"],
        description=request.json["description"],
        time_limit=int(request.json["time_limit"]),
        passing_percentage=passing_percentage,
        is_final=bool(int(request.json["is_final"]))
    )
    quizDAO.insert_one(one_quiz_object)
    
    # Question
    for question in request.json["questions"]:
        question= Question( 
            question_id = question["question_id"],
            lesson_id = request.json["lesson_id"],
            class_id = request.json["class_id"],
            course_id = request.json["course_id"],
            question = question["question"],
            options = question["options"],
            answer = int(question["answer"])
        )
        questionDAO=QuestionDAO()
        questionDAO.insert_one(question)

    # return redirect(f'http://127.0.0.1:5000/classes/{request.form["course_id"]}'
    return "Successful!"

    # except:
    #     return (
    #         jsonify({"code": 400, "msg": "Failed Creating class and course!"}),
    #         400,
    #     )

    
if __name__ == "__main__":
    app.run(port="5006", debug=True)
