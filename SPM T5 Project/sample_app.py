from flask import Flask, render_template, jsonify, request
from functools import wraps
# from flask_pymongo import PyMongo
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
app = Flask(__name__)


connection = pymongo.MongoClient(
    "18.136.194.180",
    username="spm_team",
    password="spmbestteam",
    authSource="admin",
    authMechanism="SCRAM-SHA-256",
)

db = connection["spm_aio_db"]
collection = db["class"]


# @app.route("/add",methods = ["POST"])
# def add_cls():
#     _json = request.json
#     _name = _json["name"]
#     _email = _json['email']

#display all classes
@app.route("/all_class",methods = ["GET"])
def all_class():
    all_class = collection.find() 
    resp = dumps(all_class)
    return resp


#Select one class to display according to specified id
@app.route("/all_class/<id>",methods = ["GET"])
def each_class(id):
    each_class = collection.find_one({'_id':ObjectId()}) 
    resp = dumps(all_class)
    return resp
    
#create new class
@app.route("/create_class",methods = ["POST"])
def create_class():
    json = request.json
    # course_id = "CR102"
    # class_id = "CL4"
    # trainer_name = "Chua ah huat"
    # trainer_username = "JaneBestEngineer"
    # admin_username = "LarryThePaperChaser"
    # enrolment_open_date = datetime(2021, 10, 25, 0, 0, 0, 0)
    # enrolment_close_date = datetime(2021, 11, 5, 0, 0, 0, 0)
    # start_date_time = datetime(2021, 11, 5, 0, 0, 0, 0)
    # end_date_time = datetime(2021, 11, 5, 0, 0, 0, 0)
    # class_size = 50
    # class_available_slots = 20

    if trainer_name and trainer_username and admin_username and enrolment_open_date and enrolment_close_date and start_date_time and end_date_time and class_size and class_available_slots and request.method == 'POST':
        id = collection.insert(
            {
                "_id": {"course_id": course_id, "class_id": class_id},
                "trainer_name": trainer_name,
                "trainer_username": trainer_username,
                "admin_username": admin_username,
                "enrolment_open_date": enrolment_open_date,
                "enrolment_close_date": enrolment_close_date,
                "start_date_time": start_date_time,
                "end_date_time": end_date_time,
                "class_size": class_size,
                "class_available_slots": class_available_slots,
            }
        )
        resp = jsonify("class added successfully")
        resp.status_code = 200
        return resp

    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message ={
        'status': 404,
        'message':'Not Found '+ request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp




if __name__ == "__main__":
    app.run(debug=True)