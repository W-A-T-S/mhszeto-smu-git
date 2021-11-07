from flask import Flask, jsonify, render_template,redirect
import pymongo
from flask_cors import CORS
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
from learnerDAO import LearnerDAO
from classDAO import ClassDAO

app = Flask(__name__)



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

    return render_template("removeLearner.html", learnerInfo=learner_list, course_id=course_id, class_id=class_id)


@app.route(
    "/withdraw_learners/<string:course_id>/<string:class_id>/<string:learner_username>",
    methods=["GET", "PUT", "DELETE"],
)
# Remove learner into registered class
def withdraw_learner(course_id, class_id, learner_username):

    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrolDAO.delete_one(
        class_id=class_id, course_id=course_id, learner_username=learner_username
    )

    classDAO = ClassDAO()
    classDAO.update_one(
        queryIdentifier={"_id": {"course_id": course_id, "class_id": class_id}},
        queryValues={"$inc": {"class_available_slots": 1}},
    )
 
    return redirect(f'http://18.234.140.174:5000/classes/{course_id}')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port="5004", debug=True)
