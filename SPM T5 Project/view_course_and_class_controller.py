from flask import Flask, render_template, jsonify
from courseDAO import CourseDAO
from classDAO import ClassDAO
from trainerDAO import TrainerDAO
from learnerDAO import LearnerDAO
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
import pymongo


app = Flask(__name__)


@app.route("/courses")
def courses():
    courseText = "Courses"

    # courseCollection = spmDatabase["course"]
    # result = courseCollection.find()

    courseDAO = CourseDAO()
    courses = courseDAO.find_all()
    courses_dict = []
    for course in courses:
        result = {
            "course_id": course.get_course_id(),
            "title": course.get_title(),
            "description": course.get_description(),
            "is_retired": course.get_is_retired(),
        }
        courses_dict.append(result)

    return render_template(
        "admin_view_courses.html", introText=courseText, courses=courses_dict
    )


@app.route("/classes/<courseid>")
def classes(courseid):
    classText = "Classes of " + courseid
    currentCourseId = courseid

    query = {"_id.course_id": courseid}


    classDAO = ClassDAO()
    classes = classDAO.find_query(query={"_id.course_id": courseid})


    allClassList = []

    for eachClass in classes:
        oneClassList = []

        courseId = eachClass.get_course_id()
        classId = eachClass.get_class_id()
        trainerName = eachClass.get_trainer_name()

        oneClassList.append(courseId)
        oneClassList.append(classId)
        oneClassList.append(trainerName)


        classLearnersList = []

        queryLearners = {
            "_id.course_id": courseId,
            "_id.class_id": classId,
            "is_enrolment_approved": bool("true"),
        } 
        learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
  
        learners_assignment_list = learnerAssignOrEnrolDAO.find_query(
            query=queryLearners
        )

        for aLearner_assignment in learners_assignment_list:

            learnerDAO = LearnerDAO()
            learner_details = learnerDAO.find_one(
                aLearner_assignment.get_learner_username()
            )
            classLearnersList.append(learner_details.get_name())

        oneClassList.append(classLearnersList)

        allClassList.append(
            oneClassList
        )  

    return render_template(
        "admin_view_classes.html",
        introText=classText,
        currentCourse=currentCourseId,
        classDetails=allClassList,
    )


if __name__ == "__main__":
    app.run(host= "0.0.0.0",port=5000, debug=True)

