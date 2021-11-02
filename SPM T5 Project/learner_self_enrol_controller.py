from flask import Flask, render_template, jsonify, redirect
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
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
        "learnerViewEligibleCourses.html", courses=eligible_courses_list
    )


if __name__ == "__main__":
    app.run(port=5010, debug=True)
