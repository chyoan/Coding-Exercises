# Write a Python class named Student with two attributes student_name, marks. 
# Modify the attribute values of the said class and print the original and modified values of the said attributes.

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("Chyoan", "A+")

print(student.student_name)
print(student.marks)

student.student_name = "Hyo"
student.marks = "B"

print(student.student_name)
print(student.marks)