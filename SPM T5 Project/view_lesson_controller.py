from flask import Flask, render_template, jsonify
from courseDAO import CourseDAO
from classDAO import ClassDAO
from trainerDAO import TrainerDAO
from learnerDAO import LearnerDAO
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
import pymongo

myclient = pymongo.MongoClient("mongodb://spm_team:spmbestteam@18.136.194.180:27017/")
spmDatabase = myclient["spm_aio_db"]

app = Flask(__name__)


@app.route("/view_next_lesson/<string")

def is_quiz_completed():
    
    return True
def is_materials_completed():
    return True
if (is_quiz_completed() == True and is_materials_completed()==True ):
    print ("NEXT LESSON MATERIALS")




if __name__ == "__main__":
    app.run(port=5000, debug=True)
###########
