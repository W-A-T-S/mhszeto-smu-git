from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from functools import wraps
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from os import environ
from classDAO import ClassDAO
from classDomain import Class
import dateutil.parser

app = Flask(__name__)

@app.route("/create_class/<string:course_id>", methods=["GET"])
def all_class(course_id):
    return render_template(
        "create_class.html", course_id=course_id
    )

# create new class
@app.route("/create_class", methods=["POST"])
def create_class():
    try:

        classDAO = ClassDAO()

        print(dateutil.parser.isoparse(request.form["enrolment_open_date"]))
        print(type(request.form["enrolment_open_date"]))
        # print("------------------------------------------------")
        # print(request.form)
        
        one_class_object = Class(
            course_id=request.form["course_id"].upper(),
            class_id=request.form["class_id"].upper(),
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


        return redirect(f'http://18.234.140.174:5000/classes/{request.form["course_id"]}')
    except:
        return (
            jsonify({"code": 400, "msg": "Failed Creating class and course!"}),
            400,
        )


if __name__ == "__main__":
    app.run(host= "0.0.0.0",port="5003", debug=True)
