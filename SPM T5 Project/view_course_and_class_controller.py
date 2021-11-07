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

    # classCollection = spmDatabase["class"]
    # learnerCollection = spmDatabase["learner"]
    # learnersEnrolledCollection = spmDatabase["learnerAssignOrEnrol"]

    query = {"_id.course_id": courseid}
    # resultQuery = classCollection.find(query)

    classDAO = ClassDAO()
    classes = classDAO.find_query(query={"_id.course_id": courseid})
    # print(classes[0].get_class_id())

    allClassList = []

    for eachClass in classes:
        oneClassList = []

        courseId = eachClass.get_course_id()
        classId = eachClass.get_class_id()
        trainerName = eachClass.get_trainer_name()

        oneClassList.append(courseId)
        oneClassList.append(classId)
        oneClassList.append(trainerName)

        # trainerUsername = eachClass["trainer_username"]         #Getting trainer username and querying for trainer's name
        # queryTrainer = { "_id.username" : trainerUsername }
        # resultQueryTrainer = learnerCollection.find(queryTrainer)
        # for trainer in resultQueryTrainer:
        #     oneClassList.append(trainer["name"])

        # learners assigned or enrolled
        classLearnersList = []

        queryLearners = {
            "_id.course_id": courseId,
            "_id.class_id": classId,
            "is_enrolment_approved": bool("true"),
        }  # Getting class' learners' usernames
        # resultQueryLearners = learnersEnrolledCollection.find(queryLearners)
        learnerAssignOrEnrolDAO = LearnerAssignOrEnrolDAO()
        # learners is a list
        learners_assignment_list = learnerAssignOrEnrolDAO.find_query(
            query=queryLearners
        )

        for aLearner_assignment in learners_assignment_list:

            # Getting learners' names from their usernames

            # taking learner username that was queried by learnerAssignOrEnrol and search learner information with queried username

            learnerDAO = LearnerDAO()
            learner_details = learnerDAO.find_one(
                aLearner_assignment.get_learner_username()
            )
            classLearnersList.append(learner_details.get_name())

        oneClassList.append(classLearnersList)

        allClassList.append(
            oneClassList
        )  # Appending the each-class sublist into the main all-classes list

    return render_template(
        "admin_view_classes.html",
        introText=classText,
        currentCourse=currentCourseId,
        classDetails=allClassList,
    )


if __name__ == "__main__":
    app.run(host= "0.0.0.0",port=5000, debug=True)
###########
