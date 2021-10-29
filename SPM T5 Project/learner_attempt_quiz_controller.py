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

app = Flask(__name__,template_folder ="./Templates" )

@app.route("/view_quiz/<string:class_id>/<string:course_id>/<string:lesson_id>")
def view_quiz(class_id,course_id,lesson_id):
    return render_template("takequiz.html")



# @app.route("attempt_quiz/<string:class_id>/<string:course_id>/<string:lesson_id>")
# def 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5008, debug=True)
