# Write a Python program to create an instance of a specified class and display the namespace of the said instance.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
person = Person("Chyoan", 19)

print(person.__dict__)