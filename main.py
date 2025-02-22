#FORMULA FOR DICT COMPREHENSIONS
#new_dict {new_key:new value  for item in list if test}
# Looping within another dictionary formula
# new_dict {new_key:new value  for (key, value) in dict.items()}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student:random.randint(1,100) for student in names}

print(students_score)

#DICT COMPREHENSION LOOPING INTO A DICTIONARY
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)