# from materialDAO import MaterialDAO

# materialDAO=MaterialDAO()
# obj_list=materialDAO.find_query(query={"_id.class_id":"CL1", "_id.course_id":"CR101", "_id.lesson_id":"L1"})
# print(obj_list[1].get_title())
# print("--------------------------")

# obj=materialDAO.find_one(class_id="CL1", course_id="CR101", lesson_id="L1", material_id="M1")
# print(obj.get_title())



'''
from materialCheckDAO import MaterialCheckDAO

materialCheckDAO = MaterialCheckDAO()

obj_list=materialCheckDAO.find_query(query={"_id.class_id":"CL1", "_id.course_id":"CR101", "_id.lesson_id":"L1", "_id.learner_username":"JohnSmithTheMan"})
print(obj_list[0].get_material_id())
print(obj_list[0].get_is_material_completed())
print(obj_list[1].get_material_id())
print(obj_list[1].get_is_material_completed())

obj=materialCheckDAO.find_one(class_id="CL1", course_id="CR101", lesson_id="L1", material_id="M1", learner_username="JohnSmithTheMan")
print(obj.get_material_id())
print(obj.get_is_material_completed())

query={"_id.material_id":"M2", "_id.class_id":"CL1", "_id.course_id":"CR101", "_id.lesson_id":"L1", "_id.learner_username":"JohnSmithTheMan"}
new_value={ "$set": { "is_material_completed": False } }
test = materialCheckDAO.update_one(query, new_value)
'''



'''
from quizAttemptDAO import QuizAttemptDAO
from quizAttemptDomain import QuizAttempt
quizAttemptDAO = QuizAttemptDAO()

obj_list=quizAttemptDAO.find_query(query={"_id.class_id":"CL1", "_id.course_id":"CR101", "_id.learner_username":"JohnSmithTheMan"})
print(obj_list[0].get_quiz_attempt_id())
print(obj_list[0].get_marks_awarded())
print(obj_list[0].get_is_passed())

print(obj_list[1].get_quiz_attempt_id())
print(obj_list[1].get_marks_awarded())
print(obj_list[1].get_is_passed())

obj=quizAttemptDAO.find_one(quiz_attempt_id="QA1", course_id="CR101", class_id="CL1", lesson_id=None, learner_username="JohnSmithTheMan")
print(obj.get_quiz_attempt_id())
print(obj.get_marks_awarded())
print(obj.get_is_passed())

testInsertQuizAttempt = QuizAttempt (
    quiz_attempt_id="QA4", 
    course_id="CR102", 
    class_id="CL2", 
    lesson_id="L1", 
    learner_username="JohnSmithTheMan",
    marks_awarded=90,
    is_passed=False
)

obj = quizAttemptDAO.insert_one(testInsertQuizAttempt)
'''