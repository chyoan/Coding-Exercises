# Write a Python function student_data () that will print the ID of a student (student_id). 
# If the user passes an argument student_name or student_class the function will print the student name and class.

def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")

    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}")

student_data("ID2024")
student_data("ID2024", student_name="Chyoan", student_class="Star")