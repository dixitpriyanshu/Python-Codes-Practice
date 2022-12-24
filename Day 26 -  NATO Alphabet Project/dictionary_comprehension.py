import random

names = ["Alex", "Beth", "Caroline", "Dave", "Escanor", "Leonard"]

#########  Format for Dictionary Comprehension
######     new_dict = {new_key:new_value for item in list}

#####    Dictionary Copmprehension from list

students_scores = {student: random.randint(0,100) for student in names}
print(students_scores)

##############     Dictionary Comprehension from Dictionary

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)