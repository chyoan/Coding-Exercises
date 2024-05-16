# Write a Python program to convert GPAs to letter grades according to the following table:

def convert_gpa(gpas):
    grades = []
    for gpa in gpas:
        if gpa >= 4.0:
            grades.append('A+')
        elif gpa >= 3.7:
            grades.append('A')
        elif gpa >= 3.4:
            grades.append('A-')
        elif gpa >= 3.0:
            grades.append('B+')
        elif gpa >= 2.7:
            grades.append('B')
        elif gpa >= 2.4:
            grades.append('B-')
        elif gpa >= 2.0:
            grades.append('C+')
        elif gpa >= 1.7:
            grades.append('C')
        elif gpa >= 1.4:
            grades.append('C-')
        else:
            grades.append('F')
    return grades

gpa1 = [4.0, 3.5, 3.8] # ['A+', 'A-', 'A']
gpa2 = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0] # ['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']

print(convert_gpa(gpa1))
print(convert_gpa(gpa2))