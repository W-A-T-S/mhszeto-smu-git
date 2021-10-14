from flask import Flask, jsonify, render_template
import pymongo
from flask_cors import CORS

app = Flask(__name__) 
connection = pymongo.MongoClient(
    "18.136.194.180",
    username="spm_team",
    password="spmbestteam",
    authSource="admin",
    authMechanism="SCRAM-SHA-256",
)

db = connection["spm_aio_db"]
CORS(app)

course_collection = db['course']
coursereq_collection = db['coursePrerequisite']
learner_collection = db['learner']
class_collection = db['class']
complete_collection = db['learnerAssignOrEnrol']

searchcourse="CR102"
theclass="CL1"
thelearner="BobTheGuy"
theadmin="LarryThePaperChaser"


#return back learners if the course does not require prerequisite
noreq=""

def getalllearners():
    alllearner = learner_collection.find({})
    return render_template('assign.html',  learners = alllearner)

#before removing check if p-req is met by the learner
#so course needs to be checked for pre-req first
#  course->learner->getLearner()->removeSuccess

#Check if there is a req can combine with getreq()
def checkreq(): #can reuse for the enrollment shop page
    reqresults = coursereq_collection.find({"_id.course_id":searchcourse})
    if (len(list(reqresults))>0):
        noreq=False
        return noreq

#Step 1 check if course require pre-req
def getreq(): #can reuse for the enrollment shop page
    reqresult = coursereq_collection.find({"_id.course_id":searchcourse})
    if reqresult:
        for item in reqresult:
            req=item['_id']['course_prerequisite']
            return req

#Step 2 check if learner complete pre-req
def checklearner():
    reqs=getreq()
    coursecomplete = complete_collection.find({"_id.course_id":reqs,"is_completed": bool("true")})
    #print(coursecomplete)
    for completedLearner in coursecomplete:
        learnerUsername = completedLearner["_id"]["learner_username"]
        return learnerUsername

#get the individual
def getlearner():
    learnerid=checklearner()
    learnerdetails = learner_collection.find({"_id.username":learnerid})
    #for bLearner in learnerdetails:
        #return jsonify(bLearner)
    return render_template('removeLearner.html',  learners = learnerdetails)

@app.route('/learners')
#step 3: get all the learner details for display
def choosefun():
    noreqr=checkreq()
    if noreqr==False:
        return getlearner() 
    else:
        return getalllearners()
    

#Remove learner into registered class          
def update_learner_class(course_id,class_id,learner_username,admin_username):
    classenroll = {"is_enrolment_approved": bool("true"), "is_completed": bool("true"), "_id":{"class_id": class_id,"course_id":course_id,
		"learner_username": learner_username,
        "admin_username": admin_username
	}}
    complete_collection.update_one(classenroll,{'$set':classenroll},upsert=True)
    msg="Remove Learner Successful"
    goback="https://localhost:5000/learners"
    return render_template('removeLearner.html', successmsg=msg, backlink=goback)
        #return str("Complete")
    return str("Cannot update, due to no vacancies")


