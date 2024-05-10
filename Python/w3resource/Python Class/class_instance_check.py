# Write a Python program to create two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass

class Marks:
    pass

student = Student()
marks = Marks()

print(isinstance(student, Student))
print(isinstance(student, Marks))
print(isinstance(marks, Student))
print(isinstance(marks, Marks))

print(issubclass(Student, object))
print(issubclass(Marks, object))