# Define a Python function student(). Using function attributes display the names of all arguments.

def student(name, course, year, section):
    return f"Name: {name}, Course: {course}, Year: {year}, Section: {section}"

print(student.__code__.co_varnames)