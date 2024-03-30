# Write a Python program to check, for each string in a given list, 
# whether the last character is an isolated letter or not. Return True otherwise False.

list1 = ['cat', 'car', 'fear', 'center']
list2 = ['ca t', 'car', 'fea r', 'cente r']

def check_list(lst):
    result = []
    for word in lst:
        if word[-1].isalpha() and word[-2] == ' ':
            result.append(True)
        else:
            result.append(False)
    return result

print(check_list(list1))
print(check_list(list2))