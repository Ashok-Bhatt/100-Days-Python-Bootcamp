import random

students = ["Ashok", "Irfan", "Chetan", "Ankit", "Tushar"]
students_score = {student:random.randint(0,100) for student in students}
passed_students_score = {student:score for (student,score) in students_score.items() if score>=60}

print("Score of students: ")
for item in students_score.items():
    print(item)

print("\nScore of passed students: ")
for item in passed_students_score.items():
    print(item)