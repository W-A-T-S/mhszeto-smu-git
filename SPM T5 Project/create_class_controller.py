from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from functools import wraps

# from flask_pymongo import PyMongo
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from os import environ
from classDAO import ClassDAO
from classDomain import Class
import dateutil.parser

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://spm_team:spmbestteam@18.136.194.180:27017/")
spmDatabase = myclient["spm_aio_db"]

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get(
    "mongodb://spm_team:spmbestteam@18.136.194.180:27017/"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connection = pymongo.MongoClient(
    "18.136.194.180",
    username="spm_team",
    password="spmbestteam",
    authSource="admin",
    authMechanism="SCRAM-SHA-256",
)
db = connection["spm_aio_db"]
collection = db["class"]

# display all classes
@app.route("/create_class/<string:course_id>", methods=["GET"])
def all_class(course_id):
    all_class = collection.find()
    return render_template(
        "create_class.html", all_class=all_class, course_id=course_id
    )


# # Select one class to display according to specified id
# @app.route("/each_class/<id>", methods=["GET"])
# def each_class(id):
#     each_class = collection.find_one({"_id": ObjectId()})
#     resp = dumps(all_class)
#     return resp


# create new class
@app.route("/create_class", methods=["POST"])
def create_class():
    # try:

    classDAO = ClassDAO()

    print(dateutil.parser.isoparse(request.form["enrolment_open_date"]))
    print(type(request.form["enrolment_open_date"]))

    one_class_object = Class(
        course_id=request.form["course_id"],
        class_id=request.form["class_id"],
        trainer_name=None,
        trainer_username=None,
        # KIV admin username can be hardcoded
        admin_username=request.form["admin_username"],
        enrolment_open_date=dateutil.parser.isoparse(
            request.form["enrolment_open_date"]
        ),
        enrolment_close_date=dateutil.parser.isoparse(
            request.form["enrolment_close_date"]
        ),
        start_date_time=dateutil.parser.isoparse(request.form["start_date_time"]),
        end_date_time=dateutil.parser.isoparse(request.form["end_date_time"]),
        class_size=int(request.form["class_size"]),
        class_available_slots=int(request.form["class_available_slots"]),
    )

    classDAO.insert_one(one_class_object)

    return redirect(f'http://127.0.0.1:5000/classes/{request.form["course_id"]}')

    # # except:
    # return (
    #     jsonify({"code": 400, "msg": "Failed Creating class and course!"}),
    #     400,
    # )


if __name__ == "__main__":
    app.run(port="5003", debug=True)
