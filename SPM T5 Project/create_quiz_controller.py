from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from functools import wraps

# from flask_pymongo import PyMongo
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from os import environ
from quizDAO import QuizDAO
from quizDomain import Quiz
import dateutil.parser

app = Flask(__name__)


# create new quiz
@app.route("/create_quiz", methods=["POST"])
def create_quiz():
    # try:

    quizDAO = QuizDAO()
    passing_percentage=int(request.form["passing_percentage"])
    lesson_id=request.form["lesson_id"]
    if bool(int(request.form["is_final"])):
        lesson_id=None
    else: 
        passing_percentage=0

    one_quiz_object = Quiz(
        class_id=request.form["class_id"],
        course_id=request.form["course_id"],
        lesson_id=lesson_id,
        title=request.form["title"],
        description=request.form["description"],
        time_limit=int(request.form["time_limit"]),
        passing_percentage=passing_percentage,
        is_final=bool(int(request.form["is_final"]))
    )

    quizDAO.insert_one(one_quiz_object)

    # return redirect(f'http://127.0.0.1:5000/classes/{request.form["course_id"]}')
    return "Successful!"

    # except:
    #     return (
    #         jsonify({"code": 400, "msg": "Failed Creating class and course!"}),
    #         400,
    #     )


if __name__ == "__main__":
    app.run(port="5006", debug=True)
