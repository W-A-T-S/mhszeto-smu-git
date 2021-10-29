from flask import Flask, render_template, jsonify, redirect
from courseDAO import CourseDAO
from classDAO import ClassDAO
from trainerDAO import TrainerDAO
from learnerDAO import LearnerDAO
from materialCheckDAO import MaterialCheckDAO
from quizAttemptDAO import QuizAttemptDAO
from lessonDAO import LessonDAO
from materialDAO import MaterialDAO

app = Flask(__name__,template_folder ="./Templates" )


#@app.route("/view_next_lesson/<string:lesson_id>/<string:class_id>/<string:course_id>/<string:learner_username>")
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
        return True
    else:
        return False


@app.route("/view_lesson/<string:class_id>/<string:course_id>/<string:learner_username>")
def view_lessons(class_id, course_id, learner_username):
    lessonDAO = LessonDAO()
    many_lesson_object = lessonDAO.find_query(query={"_id.class_id": class_id, "_id.course_id": course_id})
    materialCheckDAO= MaterialCheckDAO()
    
    lesson_list = [] 
    for one_lesson_object in many_lesson_object:
        
        check_completed_previous_lesson = view_next_lesson(one_lesson_object.get_lesson_id(), class_id, course_id, learner_username)
        if check_completed_previous_lesson == False:
            break
        one_lesson_dict={
            "lesson_id": one_lesson_object.get_lesson_id(),
            "title": one_lesson_object.get_title(),
            "description": one_lesson_object.get_description(),
            "learner_username": learner_username,
            "class_id": class_id,
            "course_id": course_id,
            "materials":[]
        }
        materialDAO = MaterialDAO()
        many_materialObject = materialDAO.find_query(query={"_id.class_id": class_id, "_id.course_id": course_id, "_id.lesson_id":one_lesson_object.get_lesson_id()})
        
        for one_materialObject in many_materialObject:
            
            material_id = one_materialObject.get_material_id()
            material_title = one_materialObject.get_title()
            material_type = one_materialObject.get_type()
            material_url = one_materialObject.get_url()
            material_description = one_materialObject.get_description()
            is_completed = materialCheckDAO.find_one(class_id, course_id, one_lesson_object.get_lesson_id(), material_id, learner_username).get_is_material_completed()
            one_lesson_dict["materials"].append({"material_id": material_id, "title": material_title, "description": material_description, "type":material_type , "url": material_url,"is_completed": is_completed})
        
        lesson_list.append(one_lesson_dict)
    return render_template("view_lesson.html", lessons=lesson_list)


@app.route("/update_material_completed/<string:material_id>/<string:class_id>/<string:course_id>/<string:lesson_id>/<string:learner_username>")
def update_material_completed(material_id, class_id, course_id, lesson_id, learner_username):
    materialCheckDAO = MaterialCheckDAO()
    query={"_id.material_id": material_id, "_id.class_id": class_id, "_id.course_id": course_id, "_id.lesson_id": lesson_id, "_id.learner_username": learner_username}
    new_value={ "$set": { "is_material_completed": True } }
    update_material_completion = materialCheckDAO.update_one(query, new_value)
    return "success"

@app.route("/update_material_incomplete/<string:material_id>/<string:class_id>/<string:course_id>/<string:lesson_id>/<string:learner_username>")
def update_material_incomplete(material_id, class_id, course_id, lesson_id, learner_username):
    print("I am here")
    materialCheckDAO = MaterialCheckDAO()
    query={"_id.material_id": material_id, "_id.class_id": class_id, "_id.course_id": course_id, "_id.lesson_id": lesson_id, "_id.learner_username": learner_username}
    new_value={ "$set": { "is_material_completed": False } }
    update_material_completion = materialCheckDAO.update_one(query, new_value)
    return "success"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5009, debug=True)

