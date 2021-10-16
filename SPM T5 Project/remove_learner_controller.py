from flask import Flask, jsonify, render_template
import pymongo
from flask_cors import CORS
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
from learnerDAO import LearnerDAO
from classDAO import ClassDAO

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

course_collection = db["course"]
coursereq_collection = db["coursePrerequisite"]
learner_collection = db["learner"]
class_collection = db["class"]
complete_collection = db["learnerAssignOrEnrol"]

searchcourse = "CR102"
theclass = "CL1"
thelearner = "BobTheGuy"
theadmin = "LarryThePaperChaser"


# return back learners if the course does not require prerequisite
noreq = ""


def getalllearners(course_id, class_id):
    alllearner = learner_collection.find({})
    return render_template("admin.html", learners=alllearner)


# before removing check if p-req is met by the learner
# so course needs to be checked for pre-req first
#  course->learner->getLearner()->removeSuccess

# Check if there is a req can combine with getreq()
# def checkreq():
# reqresults = coursereq_collection.find({"_id.course_id": searchcourse})
# if len(list(reqresults)) > 0:
# noreq = False
# return noreq


# # Step 1 check if course require pre-req
# def getreq():
#     reqresult = coursereq_collection.find({"_id.course_id": searchcourse})
#     if reqresult:
#         for item in reqresult:
#             req = item["_id"]["course_prerequisite"]
#             return req
# # Step 2 check if learner complete pre-req
# def checklearner():
#     reqs = getreq()
#     coursecomplete = complete_collection.find(
#         {"_id.course_id": reqs, "is_completed": bool("true")}
#     )
#     # print(coursecomplete)
#     for completedLearner in coursecomplete:
#         learnerUsername = completedLearner["_id"]["learner_username"]
#         return learnerUsername
# # get the individual
# def getlearner():
#     learnerid = checklearner()
#     learnerdetails = learner_collection.find({"_id.username": learnerid})
#     # for bLearner in learnerdetails:
#     # return jsonify(bLearner)
#     return render_template("removeLearner.html", learners=learnerdetails)
# @app.route("/learners")
# step 3: get all the learner details for display
# def choosefun():
# noreqr = checkreq()
# if noreqr == False:
# return getlearner()
# else:
# return getalllearners()


@app.route(
    "/displayclasslearner/<string:course_id>/<string:class_id>",
    methods=["GET"],
)
def display_class_course_information(course_id, class_id):

    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()

    many_assignment_objects = learnerAssignOrEnrolDAO.find_query(
        query={"_id.course_id": course_id, "_id.class_id": class_id}
    )
    
    learner_list = []
    for one_assignment_object in many_assignment_objects:
        learnerDAO = LearnerDAO()
        learner_obj = learnerDAO.find_one( learner_username=one_assignment_object .get_learner_username())

        learner_list.append(
            {"username": learner_obj.get_username(), "name": learner_obj.get_name()}
        )

    return render_template("removeLearner.html", learnerInfo=learner_list)


@app.route(
    "/withdraw_learners/<string:course_id>/<string:class_id>/<string:learner_username>",
    methods=["GET", "PUT", "DELETE"],
)
# Remove learner into registered class
def withdraw_learner(course_id, class_id, learner_username):
    # try
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrolDAO.delete_one(
        class_id=class_id, course_id=course_id, learner_username=learner_username
    )

    classDAO = ClassDAO()
    classDAO.update_one(
        queryIdentifier={"_id": {"course_id": course_id, "class_id": class_id}},
        queryValues={"$inc": {"class_available_slots": -1}},
    )
    # except

    return "Delete Learner Successful"


if __name__ == "__main__":
    app.run(port="5004", debug=True)
