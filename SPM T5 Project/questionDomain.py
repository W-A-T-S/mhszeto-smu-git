class Question:
    def __init__(self, question_id="",lesson_id="",class_id="", course_id="",  question="", options=[], answer=0):
        self._question_id = question_id 
        self._lesson_id = lesson_id
        self._class_id = class_id
        self._course_id = course_id    
        self._question = question
        self._options = options
        self._answer = answer

    def get_question_id(self):
        return self._question_id

    def get_lesson_id(self):
        return self._lesson_id

    def get_class_id(self):
        return self._class_id

    def get_course_id(self):
        return self._course_id
        
    def get_question(self):
        return self._question

    def get_options(self):
        return self._options

    def get_answer(self):
        return self._answer
