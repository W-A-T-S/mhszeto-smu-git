from flask import Flask,jsonify

class Class:
    def signup(self):
        my_class = {
            "Class ID":"",
            "Trainer usernam":"",
            "Admin username":"",
            "Enrolment Open":"",
            "Enrolment Close":"",
            "Start date":"",
            "End date":"",
            "Start time":"",
            "End time":"",
            "Class Size":"" 
        }

        return jsonify(user),200