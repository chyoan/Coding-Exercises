# Write a Python class named Student with two attributes: student_id, student_name. 
# Add a new attribute: student_class. 
# Create a function to display all attributes and their values in the Student class.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    def display_attributes(self):
        print(self.__dict__)

student = Student("ID2024", "Chyoan")

student.student_class = "Star"
student.display_attributes()