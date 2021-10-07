
class Class:
    def __init__(self,
                 class_id="",
                 course_id="",
                 trainer_username="",
                 trainer_name="",
                 admin_username="",
                 enrolment_open_date="",
                 enrolment_close_date="",
                 start_date_time="",
                 end_date_time="",
                 class_size="",
                 class_available_slots=""):
        self.__class_id = class_id
        self.__course_id = course_id
        self.__trainer_username = trainer_username
        self.__trainer_name = trainer_name
        self.__admin_username = admin_username
        self.__enrolment_open_date = enrolment_open_date
        self.__enrolment_close_date = enrolment_close_date
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__class_size = class_size
        self.__class_available_slots = class_available_slots

    def get_class_id(self):
        return self.__class_id

    def get_course_id(self):
        return self.__course_id

    def get_trainer_username(self):
        return self.__trainer_username

    def get_trainer_name(self):
        return self.__trainer_name

    def get_admin_username(self):
        return self.__admin_username

    def get_enrolment_open_date(self):
        return self.__enrolment_open_date

    def get_enrolment_close_date(self):
        return self.__enrolment_close_date

    def get_start_date_time(self):
        return self.__start_date_time

    def get_end_date_time(self):
        return self.__end_date_time

    def get_class_size(self):
        return self.__class_size

    def get_class_available_slots(self):
        return self.__class_available_slots
