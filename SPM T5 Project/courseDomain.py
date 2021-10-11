class Course:
    def __init__(
        self, course_id="", title="", description="", is_retired="", admin_username=""
    ):
        self._course_id = course_id
        self._title = title
        self._description = description
        self._is_retired = is_retired
        self._admin_username = admin_username

    def get_course_id(self):
        return self._course_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_is_retired(self):
        return self._is_retired

    def get_admin_username(self):
        return self._admin_username
