class QuestionAttempt:
    def __init__(
        self,
        question_id="",
        question_attempt_id="",
        quiz_attempt_id="",
        lesson_id="",
        class_id="",
        course_id="",
        learner_username="",
        selected_option=0,
        is_correct=False,
    ):
        self._question_attempt_id = question_attempt_id
        self._quiz_attempt_id = quiz_attempt_id
        self._question_id = question_id
        self._lesson_id = lesson_id
        self._class_id = class_id
        self._course_id = course_id
        self._learner_username = learner_username
        self._selected_option = selected_option
        self._is_correct = is_correct

    def get_question_id(self):
        return self._question_id

    def get_question_attempt_id(self):
        return self._question_attempt_id

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

    def get_selected_option(self):
        return self._selected_option

    def get_is_correct(self):
        return self._is_correct
