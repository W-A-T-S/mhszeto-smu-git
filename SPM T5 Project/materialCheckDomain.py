class MaterialCheck:
    def __init__(self, material_id="", lesson_id="", course_id="", class_id="", learner_username="", is_material_completed=""):
        self._material_id = material_id
        self._lesson_id = lesson_id
        self._course_id = course_id
        self._class_id = class_id
        self._learner_username = learner_username
        self._is_material_completed = is_material_completed


    def get_material_id(self):
        return self._material_id

    def get_lesson_id(self):
        return self._lesson_id

    def get_class_id(self):
        return self._class_id

    def get_course_id(self):
        return self._course_id
        
    def get_learner_username(self):
        return self._learner_username

    def get_is_material_completed(self):
        return self._is_material_completed
