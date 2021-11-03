from flask import Flask, render_template, jsonify, redirect
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
from learnerAssignOrEnrolDomain import LearnerAssignOrEnrol
from learnerDAO import LearnerDAO
from courseDAO import CourseDAO
from classDAO import ClassDAO
import datetime

app = Flask(__name__)


@app.route("/view_eligible_courses/<string:learner_username>")
def view_eligible_courses(learner_username):
    courseDAO = CourseDAO()
    many_courses = courseDAO.find_all()

    # learner completed course
    learnerAssignOrEnrol = LearnerAssignOrEnrolDAO()
    learner_completed_courses_object = learnerAssignOrEnrol.find_query(
        query={"_id.learner_username": learner_username, "is_completed": True}
    )
    learner_completed_list = []
    for learner_one_completed_courses_object in learner_completed_courses_object:
        course_id = learner_one_completed_courses_object.get_course_id()
        learner_completed_list.append(course_id)

    eligible_courses_list = []
    for one_course in many_courses:

        one_course_prereq = one_course.get_course_prerequisites()
        intersection_list = []

        if len(one_course_prereq) > 0:
            intersection_list = set(one_course_prereq).intersection(
                learner_completed_list
            )

        if intersection_list == one_course_prereq or one_course_prereq == []:
            classDAO = ClassDAO()
            many_classes_object = classDAO.find_query(
                query={
                    "_id.course_id": one_course.get_course_id(),
                    "enrolment_open_date": {"$lte": datetime.datetime.now()},
                    "enrolment_close_date": {"$gte": datetime.datetime.now()},
                }
            )

            if len(many_classes_object) < 1:
                continue

            course_dict = {
                "course_id": one_course.get_course_id(),
                "title": one_course.get_title(),
                "description": one_course.get_description(),
                "classes": [],
            }

            for one_class_object in many_classes_object:
                avail_slots = one_class_object.get_class_available_slots()
                if avail_slots == 0:
                    continue
                course_dict["classes"].append(
                    {
                        "course_id": one_course.get_course_id(),
                        "class_id": one_class_object.get_class_id(),
                        "start_date_time": one_class_object.get_start_date_time(),
                        "end_date_time": one_class_object.get_end_date_time(),
                        "class_size": one_class_object.get_class_size(),
                        "avail_slots": one_class_object.get_class_available_slots(),
                    }
                )

            eligible_courses_list.append(course_dict)

    return render_template(
        "learnerViewEligibleCourses.html",
        courses=eligible_courses_list,
        learner_username=learner_username,
    )


@app.route(
    "/enrol_eligible_courses/<string:course_id>/<string:class_id>/<string:learner_username>"
)
def enrol_eligible_courses(course_id, class_id, learner_username):
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrol = LearnerAssignOrEnrol(
        learner_username=learner_username,
        admin_username=None,
        class_id=class_id,
        course_id=course_id,
        is_enrolment_approved=False,
        is_completed=False,
        is_enrolment_rejected=False,
    )

    learnerAssignOrEnrolDAO.insert_one(learnerAssignOrEnrol)
    # return render_template("learnerViewEnrolledCourses.html")
    return redirect(
        f"http://18.234.140.174:5007/view_pending_courses/{learner_username}"
    )


@app.route(
    "/withdraw_course/<string:course_id>/<string:class_id>/<string:learner_username>"
)
def withdraw_course(course_id, class_id, learner_username):
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()

    learnerAssignOrEnrolDAO.delete_one(
        class_id=class_id, course_id=course_id, learner_username=learner_username
    )
    # return render_template("learnerViewEnrolledCourses.html")
    return redirect(f"http://18.234.140.174:5007/view_enrolled_courses/{learner_username}")


if __name__ == "__main__":
    app.run(port=5010, debug=True)
