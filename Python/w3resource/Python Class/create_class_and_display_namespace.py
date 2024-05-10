# Write a Python program to create a class and display the namespace of that class.

class MyClass:
    def sample_method(self):
        return 0
    def another_sample(self):
        return 1

for namespace in MyClass.__dict__:
    print(namespace)