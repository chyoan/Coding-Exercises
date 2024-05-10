# Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. 
# Print all the attributes of the student1, student2 instances with their values in the given format.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
student1 = Student("Chyoan", 19, "BSCpE")
student2 = Student("Hyo", 19, "BSCS")

print(f"Student 1: {student1.__dict__}")
print(f"Student 2: {student2.__dict__}")