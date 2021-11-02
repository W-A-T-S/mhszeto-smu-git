from flask import Flask, render_template, jsonify, redirect
from courseDAO import CourseDAO
from classDAO import ClassDAO
from trainerDAO import TrainerDAO
from learnerDAO import LearnerDAO
from materialCheckDAO import MaterialCheckDAO
from quizAttemptDAO import QuizAttemptDAO
from lessonDAO import LessonDAO
from materialDAO import MaterialDAO
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO

app = Flask(__name__, template_folder="./Templates")


@app.route("/view_enrolled_courses/<string:learner_username>")
def view_enrolled_courses(learner_username):
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    many_learner_assign_or_enroll_object = learnerAssignOrEnrolDAO.find_query(
        query={"_id.learner_username": learner_username, "is_enrolment_approved": True}
    )
    enrolled_courses_list = []
    courseDAO = CourseDAO()
    classDAO = ClassDAO()
    for one_learner_assign_or_enroll_object in many_learner_assign_or_enroll_object:
        class_id = one_learner_assign_or_enroll_object.get_class_id()
        course_id = one_learner_assign_or_enroll_object.get_course_id()
        one_class_obj = classDAO.find_one(class_id, course_id)
        start_datetime = one_class_obj.get_start_date_time()
        end_datetime = one_class_obj.get_end_date_time()
        course_description = courseDAO.find_one(course_id).get_description()

        lesson_count = get_learner_progress(class_id, course_id, learner_username)

        enrolled_courses_dict = {
            "course_id": course_id,
            "class_id": class_id,
            "course_description": course_description,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "lesson_count": lesson_count,
            "learner_username": learner_username,
        }
        enrolled_courses_list.append(enrolled_courses_dict)

    # return render_template("view_enrolled_course.html", enrolled_courses_list)
    return render_template(
        "learnerViewEnrolledCourses.html", courses=enrolled_courses_list
    )


@app.route("/view_completed_courses/<string:learner_username>")
def view_completed_courses(learner_username):
    learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
    many_learner_assign_or_enroll_object = learnerAssignOrEnrolDAO.find_query(
        query={"_id.learner_username": learner_username, "is_completed": True}
    )
    completed_courses_list = []
    courseDAO = CourseDAO()
    classDAO = ClassDAO()
    for one_learner_assign_or_enroll_object in many_learner_assign_or_enroll_object:
        class_id = one_learner_assign_or_enroll_object.get_class_id()
        course_id = one_learner_assign_or_enroll_object.get_course_id()
        one_class_obj = classDAO.find_one(class_id, course_id)
        start_datetime = one_class_obj.get_start_date_time()
        end_datetime = one_class_obj.get_end_date_time()
        course_description = courseDAO.find_one(course_id).get_description()
        completed_courses_dict = {
            "course_id": course_id,
            "class_id": class_id,
            "course_description": course_description,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "learner_username": learner_username,
        }
        completed_courses_list.append(completed_courses_dict)

    return render_template(
        "learnerViewCompletedCourses.html", courses=completed_courses_list
    )


def get_learner_progress(class_id, course_id, learner_username):
    materialCheckDAO = MaterialCheckDAO()
    quizAttemptDAO = QuizAttemptDAO()
    lessonDAO = LessonDAO()
    tl_lesson_count = len(
        lessonDAO.find_query(
            query={"_id.class_id": class_id, "_id.course_id": course_id}
        )
    )

    lesson_count = 0

    is_lesson_quiz_completed = True
    is_all_material_checked = True

    if tl_lesson_count > 0:
        for i in range(1, tl_lesson_count + 1):

            many_materialCheckObject = materialCheckDAO.find_query(
                query={
                    "_id.lesson_id": f"L{i}",
                    "_id.class_id": class_id,
                    "_id.course_id": course_id,
                    "_id.learner_username": learner_username,
                }
            )

            for one_materialCheckObject in many_materialCheckObject:
                if one_materialCheckObject.get_is_material_completed() == False:
                    is_all_material_checked = False
                    break

            many_quiz_attempts_obj = quizAttemptDAO.find_query(
                query={
                    "_id.lesson_id": f"L{i}",
                    "_id.class_id": class_id,
                    "_id.course_id": course_id,
                    "_id.learner_username": learner_username,
                }
            )
            if len(many_quiz_attempts_obj) < 1:
                is_lesson_quiz_completed = False
                break

            if is_all_material_checked == True and is_lesson_quiz_completed == True:
                lesson_count += 1

        learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()

    else:
        tl_lesson_count = 0

    if lesson_count != 0 and tl_lesson_count != 0:
        if lesson_count == tl_lesson_count:
            learnerAssignOrEnrolDAO.update_one(
                queryIdentifier={
                    "_id.learner_username": learner_username,
                    "_id.course_id": course_id,
                    "_id.class_id": class_id,
                },
                queryValues={"$set": {"is_completed": True}},
            )
        else:
            learnerAssignOrEnrolDAO.update_one(
                queryIdentifier={
                    "_id.learner_username": learner_username,
                    "_id.course_id": course_id,
                    "_id.class_id": class_id,
                },
                queryValues={"$set": {"is_completed": False}},
            )
    return str((lesson_count / tl_lesson_count) * 100)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007, debug=True)
