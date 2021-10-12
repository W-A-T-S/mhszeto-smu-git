class LearnerAssignOrEnrol:
    def __init__(self, learner_username="", admin_username="", class_id="", course_id="", is_enrolment_approved="", is_completed=""):
        self._learner_username = learner_username
        self._admin_username = admin_username
        self._class_id = class_id
        self._course_id = course_id
        self._is_enrolment_approved = is_enrolment_approved
        self._is_completed = is_completed

    def get_learner_username(self):
        return self._learner_username
        
    def get_admin_username(self):
        return self._admin_username

    def get_class_id(self):
        return self._class_id

    def get_course_id(self):
        return self._course_id

    def get_is_enrolment_approved(self):
        return self._is_enrolment_approved

    def get_is_completed(self):
        return self._is_completed