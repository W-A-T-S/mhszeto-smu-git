from flask import Flask, render_template
import pymongo

myclient = pymongo.MongoClient("mongodb://spm_team:spmbestteam@18.136.194.180:27017/")
spmDatabase = myclient["spm_aio_db"]

app = Flask(__name__)


@app.route("/courses")
def courses():
    courseText = "Courses"

    courseCollection = spmDatabase["course"]

    result = courseCollection.find()

    return render_template("adminViewCourses.html", introText = courseText, courses = result)



@app.route("/classes/<courseid>")
def classes(courseid):
    classText = "Classes of " + courseid
    currentCourseId = courseid

    classCollection = spmDatabase["class"]
    learnerCollection = spmDatabase["learner"]
    learnersEnrolledCollection = spmDatabase["learnerAssignOrEnrol"]
    
    query = { "_id.course_id" : courseid }
    resultQuery = classCollection.find(query)

    allClassList = []

    for eachClass in resultQuery:
        oneClassList = []

        courseId = eachClass["_id"]["course_id"]
        classId = eachClass["_id"]["class_id"]
        oneClassList.append(courseId)
        oneClassList.append(classId)

        trainerUsername = eachClass["trainer_username"]         #Getting trainer username and querying for trainer's name
        queryTrainer = { "_id.username" : trainerUsername }
        resultQueryTrainer = learnerCollection.find(queryTrainer)
        for trainer in resultQueryTrainer:
            oneClassList.append(trainer["name"])

        classLearnersList = []
        queryLearners = { "_id.course_id" : courseId, "_id.class_id" : classId, "is_enrolment_approved": bool("true")}      #Getting class' learners' usernames
        resultQueryLearners = learnersEnrolledCollection.find(queryLearners)
        for aLearner in resultQueryLearners:
            learnerUsername = aLearner["_id"]["learner_username"]

            queryLearnerName = { "_id.username" : learnerUsername }         #Getting learners' names from their usernames
            resultQueryLearner = learnerCollection.find(queryLearnerName)
            for learner in resultQueryLearner:
                classLearnersList.append(learner["name"])
        
        oneClassList.append(classLearnersList)

        allClassList.append(oneClassList)      #Appending the each-class sublist into the main all-classes list

    return render_template("adminViewClasses.html", introText = classText, currentCourse = currentCourseId, classDetails = allClassList)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
