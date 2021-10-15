import pymongo
from courseDomain import Course


class CourseDAO:
    def __init__(self):
        connection = pymongo.MongoClient(
            "18.136.194.180",
            username="spm_team",
            password="spmbestteam",
            authSource="admin",
            authMechanism="SCRAM-SHA-256",
        )
        db = connection["spm_aio_db"]
        self._collection = db["course"]
        self._prerequisite_collection= db["coursePrerequisite"]

    def find_all(self):
        many_course = list(self._collection.find(dict({})))
        many_course_objects = []
        for one_course in many_course:
            many_course_prerequisite=list(self._prerequisite_collection.find(dict({"_id.course_id":one_course["_id"]["course_id"]})))
            prerequisites=[]
            #getting course prerequisites list for the specified course id
            for prerequisite in many_course_prerequisite:
                prerequisites.append(prerequisite["_id"]["course_prerequisite"])

            one_course_object = Course(
                course_id=one_course["_id"]["course_id"],
                title=one_course["title"],
                description=one_course["description"],
                is_retired=one_course["is_retired"],
                admin_username=one_course["admin_username"],
                course_prerequisites=prerequisites
            )
            many_course_objects.append(one_course_object)
        return many_course_objects

    def find_one(self, course_id):
        one_course = self._collection.find_one(dict({"_id.course_id": course_id}))
        many_course_prerequisite=list(self._prerequisite_collection.find(dict({"_id.course_id":one_course["_id"]["course_id"]})))
        prerequisites=[]
        for prerequisite in many_course_prerequisite:
                prerequisites.append(prerequisite["_id"]["course_prerequisite"])
        one_course_object = Course(
            course_id=one_course["_id"]["course_id"],
            title=one_course["title"],
            description=one_course["description"],
            is_retired=one_course["is_retired"],
            admin_username=one_course["admin_username"],
            course_prerequisites=prerequisites
        )
        return one_course_object

    