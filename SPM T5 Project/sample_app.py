from flask import Flask, render_template, jsonify, request,redirect,url_for
from flask_cors import CORS
from functools import wraps
# from flask_pymongo import PyMongo
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from os import environ
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://spm_team:spmbestteam@18.136.194.180:27017/")
spmDatabase = myclient["spm_aio_db"]

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('mongodb://spm_team:spmbestteam@18.136.194.180:27017/') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connection = pymongo.MongoClient(
    "18.136.194.180",
    username="spm_team",
    password="spmbestteam",
    authSource="admin",
    authMechanism="SCRAM-SHA-256",
)
db = connection["spm_aio_db"]
collection = db["class"]

CORS(app)





#display all classes
@app.route("/all_class",methods = ["GET"])
def all_class():
    all_class = collection.find() 
    return render_template('create_class.html', all_class = all_class)

#Select one class to display according to specified id
@app.route("/each_class/<id>",methods = ["GET"])
def each_class(id):
    each_class = collection.find_one({'_id':ObjectId()}) 
    resp = dumps(all_class)
    return resp
    
#create new class
@app.route("/create_class",methods = ["POST"])
def create_class():
    #extracting filled in forms
    json = request.json



    #inserting to MongoDB
    if request.method == 'POST':
        course_id = request.form['course_id']
        class_id = request.form['class_id']
        trainer_name = request.form['trainer_name']
        trainer_username = request.form['trainer_username']
        admin_username = request.form['admin_username']
        enrolment_open_date = datetime(2021, 10, 25, 0, 0, 0, 0)
        enrolment_close_date = datetime(2021, 11, 5, 0, 0, 0, 0)
        start_date_time = datetime(2021, 11, 5, 0, 0, 0, 0)
        end_date_time = datetime(2021, 11, 5, 0, 0, 0, 0)
        class_size = request.form['class_size']
        class_available_slots = request.form['class_available_slots']
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
        return redirect(url_for('all_class'))

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