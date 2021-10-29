from flask import Flask, render_template, jsonify
from courseDAO import CourseDAO
from classDAO import ClassDAO
from trainerDAO import TrainerDAO
from learnerDAO import LearnerDAO
from materialCheckDAO import MaterialCheckDAO
from quizAttemptDAO import QuizAttemptDAO
from lessonDAO import LessonDAO
from materialDAO import MaterialDAO

app = Flask(__name__,template_folder ="./Templates" )


@app.route("/view_next_lesson/<string:lesson_id>/<string:class_id>/<string:course_id>/<string:learner_username>")
def view_next_lesson(lesson_id, class_id, course_id, learner_username):
    materialCheckDAO= MaterialCheckDAO()
    quizAttemptDAO=QuizAttemptDAO()
    is_lesson_quiz_completed = True
    is_all_material_checked = True
    lesson_num = int(lesson_id[1:])

    for i in range(1,lesson_num):
        print(i)
        many_materialCheckObject= materialCheckDAO.find_query(query={"_id.lesson_id": f'L{i}', "_id.class_id": class_id, "_id.course_id": course_id, "_id.learner_username": learner_username})

        for one_materialCheckObject in many_materialCheckObject:
            if one_materialCheckObject.get_is_material_completed() == False:
                is_all_material_checked = False
         

        many_quiz_attempts_obj=quizAttemptDAO.find_query(query={"_id.lesson_id": f'L{i}', "_id.class_id": class_id, "_id.course_id": course_id, "_id.learner_username": learner_username})
        if(len(many_quiz_attempts_obj)<1):
            is_lesson_quiz_completed = False
            break
     

    if is_lesson_quiz_completed and is_all_material_checked:
        return "next lesson"
    else:
        return "no you slow"


@app.route("/view_lesson/<string:class_id>/<string:course_id>")
def view_lessons(class_id, course_id):
    lessonDAO = LessonDAO()
    many_lessonObject = lessonDAO.find_query(query={"_id.class_id": class_id, "_id.course_id": course_id})
    lesson_list = [] 
    for one_lesson_object in many_lesson_object:
        one_lesson_dict={
            "lesson_id": one_lesson_object.get_lesson_id(),
            "title": one_lesson_object.get_title(),
            "description": one_lesson_object.get_description(),
            "materials":[]
        }
        many_materialObject = materialDAO.find_query(query={"_id.class_id": class_id, "_id.course_id": course_id, "_id.lesson_id":one_lesson_object.get_lesson_id()})
        
        for one_materialObject in many_materialObject:
            material_id = one_materialObject.get_material_id()
            material_title = one_materialObject.get_title()
            material_type = one_materialObject.get_type()
            material_url = one_materialObject.get_url()
            material_description = one_lesson_dict.get_description()
            
            one_lesson_dict["materials"].append({"material_id": material_id, "title": material_title, "description": material_description, "type":material_type , "url": material_url})
        
        lesson_list.append(one_lesson_dict)
    return render_template("view_lesson.html", lessons=lesson_list)






if __name__ == "__main__":
    app.run(port=5000, debug=True)

