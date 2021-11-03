from flask import Flask, jsonify, render_template, redirect, request
import pymongo

# from flask_cors import CORS
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
from learnerAssignOrEnrolDomain import LearnerAssignOrEnrol
from learnerDAO import LearnerDAO
from classDAO import ClassDAO
from courseDAO import CourseDAO

app = Flask(__name__)

# CORS(app)


def checklearner_for_prereq_list(list_of_prerequisites):
    learners_who_completed_prereq_list = []
    count = 0
    for prerequisite in list_of_prerequisites:
        # e.g. COR101 ,COR102,COR103
        if len(checklearner_per_prereq_list(prerequisite)) == 0:
            return []

        else:
            learners = checklearner_per_prereq_list(prerequisite)

            if count == 0:
                learners_who_completed_prereq_list = learners
            else:
                learners_who_completed_prereq_list = (
                    learners_who_completed_prereq_list.intersection(learners)
                )

        count += 1
    # print(learners["learners_who_completed_prereq_list"])
    return learners_who_completed_prereq_list


# Step 2 check if learner complete prerequisite
def checklearner_per_prereq_list(prerequisite):

    learnerAssignOrEnrol = LearnerAssignOrEnrolDAO()
    learners_completed = list(
        learnerAssignOrEnrol.find_query(
            query={"_id.course_id": prerequisite, "is_completed": bool("true")}
        )
    )
    learners_list = []
    for learner in learners_completed:
        learners_list.append(learner.get_learner_username())
    return learners_list


def getlearner(learners_met_prerequisites, course_id, class_id):
    # learnerid=checklearner()
    # learnerdetails = learner_collection.find({"_id.username":learnerid})
    learnerDAO = LearnerDAO()
    learnersdetails = []
    for learner in learners_met_prerequisites:
        learner_obj = learnerDAO.find_one(learner_username=learner)
        learner_dict = {"name": learner_obj.get_name(), "username": learner}
        learnersdetails.append(learner_dict)

    # for bLearner in learnerdetails:
    # return jsonify(bLearner)
    return render_template(
        "assign.html", learners=learnersdetails, course_id=course_id, class_id=class_id
    )


def getalllearners(course_id, class_id):
    learnerDAO = LearnerDAO()
    # learner_collection.find({})
    alllearner = learnerDAO.find_all()
    learners_list = []
    for learner in alllearner:
        learners_list.append(
            {"name": learner.get_name(), "username": learner.get_username()}
        )
    return render_template(
        "assign.html", learners=learners_list, course_id=course_id, class_id=class_id
    )


@app.route("/assignlearners/<string:course_id>/<string:class_id>")
# step 3: get all the learner details for display
def check_if_course_needs_prereq(course_id, class_id):

    courseDAO = CourseDAO()
    course_obj = courseDAO.find_one(course_id=course_id)
    if course_obj.get_course_prerequisites():
        learners_met_prerequisites = checklearner_for_prereq_list(
            course_obj.get_course_prerequisites()
        )
        return getlearner(learners_met_prerequisites, course_id, class_id)
        # return render_template("assign.html", learners=filteredlearners)
    else:
        return getalllearners(course_id, class_id)


# Step 1: Check for class available vacancies
def getvaccancies(course_id, class_id):
    classDAO = ClassDAO()
    one_class_object = classDAO.find_one(class_id=class_id, course_id=course_id)
    res = one_class_object.get_class_available_slots()
    return int(res)


# Step 3 Add learner into registered class
def create_learner_assignment_class(
    course_id, class_id, learner_username, admin_username
):

    learnerAssignOrEnrol = LearnerAssignOrEnrol(
        learner_username=learner_username,
        admin_username=admin_username,
        class_id=class_id,
        course_id=course_id,
        is_enrolment_approved=True,
        is_completed=False,
        is_enrolment_rejected=False,
    )
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrolDAO.insert_one(learnerAssignOrEnrol)
    # complete_collection.update_one(classenroll,{'$set':classenroll},upsert=True)


@app.route(
    "/updatelearner/<string:course_id>/<string:class_id>/<string:learner_username>/<string:admin_username>",
    methods=["GET", "PUT"],
)
def update_class_course_information(
    course_id, class_id, learner_username, admin_username
):

    coursevacant = getvaccancies(course_id, class_id)
    if coursevacant > 0:
        vacleft = coursevacant - 1
        print(vacleft)
        classDAO = ClassDAO()
        classDAO.update_one(
            queryIdentifier={"_id": {"course_id": course_id, "class_id": class_id}},
            queryValues={"$set": {"class_available_slots": vacleft}},
        )
        create_learner_assignment_class(
            course_id, class_id, learner_username, admin_username
        )
        msg = "Assign Learner Successful"

        return redirect(f"http://18.234.140.174:5000/classes/{course_id}")

        # return str("Completed")
    else:
        return str("Cannot update, due to no vacancies")


@app.route(
    "/approve_learner/<string:course_id>/<string:class_id>/<string:learner_username>/<string:admin_username>",
    methods=["GET", "PUT"],
)
def approve_learner(course_id, class_id, learner_username, admin_username):
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrolDAO.delete_one(
        class_id=class_id, course_id=course_id, learner_username=learner_username
    )

    learnerAssignOrEnrol = LearnerAssignOrEnrol(
        learner_username=learner_username,
        admin_username=admin_username,
        class_id=class_id,
        course_id=course_id,
        is_enrolment_approved=True,
        is_completed=False,
        is_enrolment_rejected=False,
    )
    learnerAssignOrEnrolDAO.insert_one(learnerAssignOrEnrol)

    return redirect(
        f"http://18.234.140.174:5001/get_learner_enrolment_requests/{course_id}/{class_id}"
    )


@app.route(
    "/reject_learner/<string:course_id>/<string:class_id>/<string:learner_username>/<string:admin_username>",
    methods=["GET", "PUT"],
)
def reject_learner(course_id, class_id, learner_username, admin_username):

    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrolDAO.delete_one(
        class_id=class_id, course_id=course_id, learner_username=learner_username
    )

    learnerAssignOrEnrol = LearnerAssignOrEnrol(
        learner_username=learner_username,
        admin_username=admin_username,
        class_id=class_id,
        course_id=course_id,
        is_enrolment_approved=False,
        is_completed=False,
        is_enrolment_rejected=True,
    )
    learnerAssignOrEnrolDAO.insert_one(learnerAssignOrEnrol)

    return redirect(
        f"http://18.234.140.174:5001/get_learner_enrolment_requests/{course_id}/{class_id}"
    )


@app.route(
    "/get_learner_enrolment_requests/<string:course_id>/<string:class_id>",
    methods=["GET", "PUT"],
)
def get_learner_enrolment_requests(course_id, class_id):
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()

    many_learnersAssignOrEnrol_object = learnerAssignOrEnrolDAO.find_query(
        query={
            "_id.course_id": course_id,
            "_id.class_id": class_id,
            "is_enrolment_approved": False,
            "is_enrolment_rejected": False,
        }
    )
    learner_list = []
    for one_learnersAssignOrEnrol_object in many_learnersAssignOrEnrol_object:
        learner_username = one_learnersAssignOrEnrol_object.get_learner_username()

        learnerDAO = LearnerDAO()
        learner_obj = learnerDAO.find_one(learner_username=learner_username)
        learner_name = learner_obj.get_name()

        learner_list.append(
            {
                "learner_name": learner_name,
                "learner_username": learner_username,
                "class_id": class_id,
                "course_id": course_id,
            }
        )

    return render_template("selfenrolmentrequests.html", learners=learner_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
