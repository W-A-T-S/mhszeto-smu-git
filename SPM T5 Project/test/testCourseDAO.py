import unittest
from unittest.mock import MagicMock
import sys

sys.path.append("../../../SPM T5 Project/")
from courseDAO import CourseDAO

#testCourseDAO class - Chow Li Wei John
class testCourseDAO(unittest.TestCase):
    def setUp(self):
        self.__courseDAO = CourseDAO()

        self.__mockCourses = [
            {
                "_id": {"course_id": "CR101"},
                "title": "Introduction to Laser Printers",
                "description": "This is CR101",
                "is_retired": False,
                "admin_username" : "LarryThePaperChaser",
                "course_prerequisites": []
            },
            {
                "_id": {"course_id": "CR102"},
                "title": "Networking for Printers",
                "description": "This is CR102",
                "is_retired": True,
                "admin_username" : "JaneTheEngineer",
                "course_prerequisites": ["CR101"]
            }
        ]

        self.__mockOneCourse = {
            "_id": {"course_id": "CR102"},
            "title": "Networking for Printers",
            "description": "This is CR102",
            "is_retired": True,
            "admin_username" : "JaneTheEngineer",
            "course_prerequisites": ["CR101"]
        }


    def testFindAllCourses(self):
        mockCourse = self.__courseDAO._collection
        mockCourse.find = MagicMock(mockCourse, return_value = self.__mockCourses)
        
        courseResult = self.__courseDAO.find_all()
        self.assertEqual(len(courseResult), 2)

        idList = []
        titleList = []
        descriptionList = []
        statusList = []
        adminList = []
        coursePrerequisiteList = []

        for course in courseResult:
            idList.append(course.get_course_id())
            titleList.append(course.get_title())
            descriptionList.append(course.get_description())
            statusList.append(course.get_is_retired())
            adminList.append(course.get_admin_username())
            coursePrerequisiteList.append(course.get_course_prerequisites())

        self.assertEqual(idList, ["CR101", "CR102"])
        self.assertEqual(titleList, ["Introduction to Laser Printers", "Networking for Printers"])
        self.assertEqual(descriptionList, ["This is CR101", "This is CR102"])
        self.assertEqual(statusList, [False, True])
        self.assertEqual(adminList, ["LarryThePaperChaser", "JaneTheEngineer"])
        self.assertEqual(coursePrerequisiteList, [[], ["CR101"]])


    def testFindOneCourse(self):
        mockCourse = self.__courseDAO._collection
        mockCourse.find_one = MagicMock(mockCourse, return_value = self.__mockOneCourse)
        
        courseResult = self.__courseDAO.find_one("CR102")

        self.assertEqual(courseResult.get_course_id(), "CR102")
        self.assertEqual(courseResult.get_title(), "Networking for Printers")
        self.assertEqual(courseResult.get_description(), "This is CR102")
        self.assertEqual(courseResult.get_is_retired(), True)
        self.assertEqual(courseResult.get_admin_username(), "JaneTheEngineer")
        self.assertEqual(courseResult.get_course_prerequisites(), ["CR101"])


    def testNoCoursesFound(self):
        mockCourse = self.__courseDAO._collection
        mockCourse.find = MagicMock(mockCourse, return_value = [])

        courseResult = self.__courseDAO.find_all()
        self.assertEqual(len(courseResult), 0)


    def tearDown(self):
        self.__courseDAO = None