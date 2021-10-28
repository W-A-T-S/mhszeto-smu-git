class QuizAttempt:
    def __init__(self, quiz_attempt_id="", lesson_id="", course_id="", class_id="", learner_username="", marks_awarded="", is_passed=""):
        self._quiz_attempt_id = quiz_attempt_id
        self._lesson_id = lesson_id
        self._course_id = course_id
        self._class_id = class_id
        self._learner_username = learner_username
        self._marks_awarded = marks_awarded
        self._is_passed = is_passed


    def get_quiz_attempt_id(self):
        return self._quiz_attempt_id

    def get_lesson_id(self):
        return self._lesson_id

    def get_course_id(self):
        return self._course_id

    def get_class_id(self):
        return self._class_id
        
    def get_learner_username(self):
        return self._learner_username

    def get_marks_awarded(self):
        return self._marks_awarded
    
    def get_is_passed(self):
        return self._is_passed
