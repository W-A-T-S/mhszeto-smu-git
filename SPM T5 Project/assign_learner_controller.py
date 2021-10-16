from flask import Flask, jsonify, render_template
import pymongo
from flask_cors import CORS
from learnerAssignOrEnrolDAO import LearnerAssignOrEnrolDAO
from learnerAssignOrEnrolDomain import LearnerAssignOrEnrol
from learnerDAO import LearnerDAO
from classDAO import ClassDAO
from courseDAO import CourseDAO

app = Flask(__name__) 
connection = pymongo.MongoClient(
    "18.136.194.180",
    username="spm_team",
    password="spmbestteam",
    authSource="admin",
    authMechanism="SCRAM-SHA-256",
)

db = connection["spm_aio_db"]
CORS(app)

course_collection = db['course']
coursereq_collection = db['coursePrerequisite']
learner_collection = db['learner']
class_collection = db['class']
complete_collection = db['learnerAssignOrEnrol']

searchcourse="CR102"
theclass="CL1"
thelearner="BobTheGuy"
theadmin="LarryThePaperChaser"


#get all learners if the course does not require prerequisite
noreq=""

def checklearner_for_prereq_list(list_of_prerequisites):
    learners_who_completed_prereq_list =[]
    count=0
    for prerequisite in list_of_prerequisites:
    #e.g. COR101 ,COR102,COR103
        if len(checklearner_per_prereq_list(prerequisite)) == 0:
            return []

        else:
            learners=checklearner_per_prereq_list(prerequisite)
            
            if(count==0):
                learners_who_completed_prereq_list=learners
            else:
                learners_who_completed_prereq_list=learners_who_completed_prereq_list.intersection(learners)
        
        count+=1
    # print(learners["learners_who_completed_prereq_list"])
    return learners_who_completed_prereq_list


#Step 2 check if learner complete prerequisite
def checklearner_per_prereq_list(prerequisite):
   
    learnerAssignOrEnrol=LearnerAssignOrEnrolDAO()
    learners_completed=list(learnerAssignOrEnrol.find_query(query={"_id.course_id":prerequisite,"is_completed": bool("true")}))
    learners_list=[]
    for learner in learners_completed:
        learners_list.append(learner.get_learner_username())
    return learners_list
  

def getlearner(learners_met_prerequisites):
    #learnerid=checklearner()
    # learnerdetails = learner_collection.find({"_id.username":learnerid})
    learnerDAO=LearnerDAO()
    learnersdetails=[]
    for learner in learners_met_prerequisites:
       learner_obj=learnerDAO.find_one(learner_username=learner)
       learner_dict={"name":learner_obj.get_name(), "username":learner}
       learnersdetails.append(learner_dict)

    #for bLearner in learnerdetails:
        #return jsonify(bLearner)
    return render_template('assign.html',  learners = learnersdetails)


def getalllearners():
    alllearner = learner_collection.find({})
    return render_template('assign.html',  learners = alllearner)


@app.route('/assign_learners')
#step 3: get all the learner details for display
def check_if_course_needs_prereq():

    courseDAO=CourseDAO()
    course_obj=courseDAO.find_one(course_id=searchcourse)
    learners_met_prerequisites=checklearner_for_prereq_list(course_obj.get_course_prerequisites())
    return getlearner(learners_met_prerequisites)
    
    
    # noreqr=checkreq(course_obj.get_course_prerequisites())
    #      checklearner(course_obj.get_course_prerequisites())
    # if noreqr==False:
    #     return getlearner() 
    # else:
    #     return getalllearners()
    


#Step 1: Check for class available vacancies
def getvaccancies(course_id, class_id):
    classDAO=ClassDAO()
    one_class_object=classDAO.find_one(class_id=class_id, course_id=course_id)
    #vacanciesdetails = class_collection.find({"_id.course_id":searchcourse,"_id.class_id":theclass})
    # for vacant in one_class_object:
    res=one_class_object.get_class_available_slots()
    print("this is res",res)
    return int(res)

#Step 3 Add learner into registered class          
def create_learner_assignment_class(course_id,class_id,learner_username,admin_username):

    learnerAssignOrEnrol=LearnerAssignOrEnrol(learner_username=learner_username, admin_username=admin_username, class_id=class_id, course_id=course_id, is_enrolment_approved=True, is_completed=False)
    learnerAssignOrEnrolDAO=LearnerAssignOrEnrolDAO()
    learnerAssignOrEnrolDAO.insert_one(learnerAssignOrEnrol)
    # complete_collection.update_one(classenroll,{'$set':classenroll},upsert=True)
    
@app.route("/assign_learner/<string:course_id>/<string:class_id>/<string:learner_username>/<string:admin_username>", methods=["GET","PUT"])
def update_class_course_information(course_id,class_id,learner_username, admin_username):

    coursevacant= getvaccancies(course_id, class_id)
    if  coursevacant > 0:
        vacleft=coursevacant-1
        print(vacleft)
        classDAO=ClassDAO()
        classDAO.update_one(queryIdentifier={"_id": {
            "course_id": course_id,
            "class_id": class_id
        }}, queryValues={"$set": {
            "class_available_slots": vacleft
        }})
        create_learner_assignment_class(course_id,class_id,learner_username,admin_username)
        msg="Assign Learner Successful"
        return render_template('assign.html', successmsg=msg)
        #return str("Completed")
    else:
        return str("Cannot update, due to no vacancies")


'''

if course no need prequisite
- list all learner-done


if course need prequisite
- check if prereq completed -done
- get learner username-done
- match to get username to get full detail -done

things to do afterwards
-check vacancies
- register learner to class (insert learnerAssignOrEnrol classid) - still doing
- update class vacancy number -done
'''
'''

#@app.route("/assign_learner/<string:course_id>/<string:class_id>/<string:learner_username>/", methods=['PUT'])

#Step 1: Check for class available vacancies
def getvaccancies():
    vacanciesdetails = class_collection.find({"_id.course_id":searchcourse,"_id.class_id":theclass})
    for vacant in vacanciesdetails:
            res=vacant['class_available_slots']
            return int(res)

#Step 3 Add learner into registered class          
def update_learner_class():
    classenroll = {"is_enrolment_approved": bool("true"), "is_completed": bool("false"), "_id":{"class_id": theclass,"course_id":searchcourse,
		"learner_username": thelearner,
        "admin_username": theadmin
	}}
    complete_collection.update_one(classenroll,{'$set':classenroll},upsert=True)
    
@app.route('/learners')

def update_class_course_information():
    coursevacant= getvaccancies()
    if  coursevacant > 0:
        class_collection.update_one({"_id": {
            "course_id": searchcourse,
            "class_id": theclass
        }}, {"$set": {
            "class_available_slots": coursevacant-1
        }})
        update_learner_class()
        msg="Assign Learner Successful"
        return render_template('assign.html', successmsg=msg)
        #return str("Completed")
    else:
        return str("Cannot update, due to no vacancies")
'''






if __name__ == '__main__':
    app.run(debug=True)