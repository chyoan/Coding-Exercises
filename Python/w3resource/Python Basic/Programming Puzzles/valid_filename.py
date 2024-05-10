# A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should have at most three digits, no additional periods. 
# Write a Python program to create a list of True/False that determine whether candidate filename is valid or not.

def valid_or_not(file_names):
    file_extensions = ['.txt', '.exe', '.jpg', '.png', '.dll']
    result = []
    for file_name in file_names:
        if '.' not in file_name:
            result.append("No")
            continue
        name, ext = file_name.rsplit('.', 1)
        ext = '.' + ext
        if name != '' and ext in file_extensions and sum(ch.isdigit() for ch in name) <= 3 and name.count('.') == 0:
            result.append("Yes")
        else:
            result.append("No")
    return result

list1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe'] # ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
list2 = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java'] # ['No', 'Yes', 'No', 'No', 'No']

print(valid_or_not(list1))
print(valid_or_not(list2))