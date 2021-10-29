import pymongo

from classDomain import Class


class ClassDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["class"]

    def find_all(self):
        many_class = list(self._collection.find(dict({})))
        many_class_objects = []
        for one_class in many_class:
            one_class_object = Class(
                class_id=one_class["_id"]["class_id"],
                course_id=one_class["_id"]["course_id"],
                trainer_username=one_class["trainer_username"],
                trainer_name=one_class["trainer_name"],
                admin_username=one_class["admin_username"],
                enrolment_open_date=one_class["enrolment_open_date"],
                enrolment_close_date=one_class["enrolment_close_date"],
                start_date_time=one_class["start_date_time"],
                end_date_time=one_class["end_date_time"],
                class_size=one_class["class_size"],
                class_available_slots=one_class["class_available_slots"],
            )
            many_class_objects.append(one_class_object)
        return many_class_objects

    def find_one(self, class_id, course_id):
        one_class = self._collection.find_one(
            dict({"_id.course_id": course_id, "_id.class_id": class_id})
        )

        one_class_object = Class(
            class_id=one_class["_id"]["class_id"],
            course_id=one_class["_id"]["course_id"],
            trainer_username=one_class["trainer_username"],
            trainer_name=one_class["trainer_name"],
            admin_username=one_class["admin_username"],
            enrolment_open_date=one_class["enrolment_open_date"],
            enrolment_close_date=one_class["enrolment_close_date"],
            start_date_time=one_class["start_date_time"],
            end_date_time=one_class["end_date_time"],
            class_size=one_class["class_size"],
            class_available_slots=one_class["class_available_slots"],
        )
        
        return one_class_object

    def find_query(self, query):
        many_class = list(self._collection.find(dict(query)))

        many_class_objects = []
        if len(many_class) > 0:
            for one_class in many_class:
                one_class_object = Class(
                    class_id=one_class["_id"]["class_id"],
                    course_id=one_class["_id"]["course_id"],
                    trainer_username=one_class["trainer_username"],
                    trainer_name=one_class["trainer_name"],
                    admin_username=one_class["admin_username"],
                    enrolment_open_date=one_class["enrolment_open_date"],
                    enrolment_close_date=one_class["enrolment_close_date"],
                    start_date_time=one_class["start_date_time"],
                    end_date_time=one_class["end_date_time"],
                    class_size=one_class["class_size"],
                    class_available_slots=one_class["class_available_slots"],
                )
                many_class_objects.append(one_class_object)
        return many_class_objects

    def update_one(self, queryIdentifier, queryValues):
        res = self._collection.update_one(queryIdentifier, queryValues)
        return res

#creating a class into mongodb 
    def insert_one(self,one_class_object):

        self._collection.insert(
            {
                "_id": {"course_id": one_class_object.get_course_id(), "class_id": one_class_object.get_class_id()},
                "trainer_name": one_class_object.get_trainer_name(),
                "trainer_username": one_class_object.get_trainer_username(),
                "admin_username": one_class_object.get_admin_username(),
                "enrolment_open_date": one_class_object.get_enrolment_open_date(),
                "enrolment_close_date": one_class_object.get_enrolment_close_date(),
                "start_date_time": one_class_object.get_start_date_time(),
                "end_date_time": one_class_object.get_end_date_time(),
                "class_size": one_class_object.get_class_size(),
                "class_available_slots": one_class_object.get_class_available_slots(),
            }
        )
