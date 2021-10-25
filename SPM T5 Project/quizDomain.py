class Quiz:
    def __init__(self, class_id="", name="", course_id="", lesson_id="", title="",description="",time_limit=0, passing_percentage=0, is_final=False):
        self._class_id = class_id
        self._course_id = course_id
        self._lesson_id = lesson_id
        self._title = title
        self._description = description
        self._time_limit = time_limit
        self._passing_percentage = passing_percentage
        self._is_final = is_final

    def get_class_id(self):
        return self._class_id

    def get_course_id(self):
        return self._course_id

    def get_lesson_id(self):
        return self._lesson_id

    def get_title(self):
        return self._title
        
    def get_description(self):
        return self._description

    def get_time_limit(self):
        return self._time_limit

    def get_passing_percentage(self):
        return self._passing_percentage
        
    def get_is_final(self):
        return self._is_final
