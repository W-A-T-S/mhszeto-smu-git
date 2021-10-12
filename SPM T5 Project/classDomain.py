class Class:
    def __init__(self,course_id= '', class_id='',trainer_name='',trainer_username='',admin_username='',enrolment_open_date='',enrolment_close_date='',start_date_time='',end_date_time='',class_size=0,class_available_slots=0):

        self.__course_id = course_id
        self.__class_id = class_id
        self.__trainer_username=trainer_username 
        self.__trainer_name = trainer_name
        self.__admin_username = admin_username
        self.__enrolment_open_date = enrolment_open_date
        self.__enrolment_close_date = enrolment_close_date
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__class_size = class_size
        self.__class_available_slots= class_available_slots