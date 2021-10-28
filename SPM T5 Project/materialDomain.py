class MaterialCheck:
    def __init__(self, material_id="", lesson_id="", course_id="", class_id="", title="", description="", material_type="", url=""):
        self._material_id = material_id
        self._lesson_id = lesson_id
        self._course_id = course_id
        self._class_id = class_id
        self._title = title
        self._description = description
        self._type = material_type
        self._url = url

    def get_material_id(self):
        return self._material_id

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

    def get_type(self):
        return self._type

    def get_url(self):
        return self._url