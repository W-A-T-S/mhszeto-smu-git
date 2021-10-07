from flask import Flask, jsonify, render_template, request, send_from_directory
from classDAO import ClassDAO
from courseDAO import CourseDAO
from trainerDAO import TrainerDAO
import datetime
app = Flask(__name__, template_folder="html")


@app.route("/assign_trainer")
def display_page():
    return render_template("assign_trainer.html")


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route("/assign_trainer/json/<string:course_id>/<string:class_id>", methods=['GET'])
def get_class_course_information(course_id, class_id):
    courseDAO = CourseDAO()
    one_course = courseDAO.find_one(course_id=course_id)

    classDAO = ClassDAO()
    one_class = classDAO.find_one(class_id=class_id, course_id=course_id)

    trainerDAO = TrainerDAO()
    tr = trainerDAO.find_all()

    trainers = []
    for trainer in tr:
        num_classes_running = len(classDAO.find_query(
            query={"trainer_username": trainer.get_username(),
                   "start_date_time": {"$lte":  datetime.datetime.now()},
                   "end_date_time": {"$gte":  datetime.datetime.now()}
                   }))

        num_classes_assigned = len(classDAO.find_query(
            query={"trainer_username": trainer.get_username(),
                   }))

        trainers.append({"username": trainer.get_username(),
                        "name": trainer.get_name(),
                         "current_designation": trainer.get_current_designation(),
                         "num_classes_running": num_classes_running,
                         "num_classes_assigned": num_classes_assigned
                         })

    return jsonify({
        "code": 200,
        "data": {
            "course": {
                "id": one_course.get_course_id(),
                "title": one_course.get_title(),
            },
            "class": {
                "id": one_class.get_class_id(),
                "start_date_time": one_class.get_start_date_time(),
                "end_date_time": one_class.get_end_date_time(),
                "trainer_username": one_class.get_trainer_username(),
                "trainer_name": one_class.get_trainer_name()
            },
            "trainers": trainers
        }
    }), 200


@app.route("/assign_trainer/json/<string:course_id>/<string:class_id>", methods=['PUT'])
def update_class_course_information(course_id, class_id):
    classDAO = ClassDAO()
    classDAO.update_one(queryIdentifier={"_id": {
        "course_id": course_id,
        "class_id": class_id
    }}, queryValues={"$set": {
        "trainer_name": request.json["trainer_name"],
        "trainer_username": request.json["trainer_username"]
    }, "$currentDate": {"lastModified": True}
    }
    )

    return jsonify({
        "code": 200,
    })


if __name__ == '__main__':
    app.run(port=5001, debug=True)
