class Lesson:
    def __init__(self, lesson_id="", class_id="", course_id="",title ="", description = ""):
        self.lesson_id = lesson_id
        self.class_id = class_id
        self.course_id = course_id

    def get_lesson_id(self):
        return self._lesson_id

    def get_class_id(self):
        return self._class_id

    def get_course_id(self):
        return self._course_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description
