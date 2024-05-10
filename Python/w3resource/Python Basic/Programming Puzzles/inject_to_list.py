# Given a list of numbers and a number to inject, write a Python program to create a list containing that number in between each pair of adjacent numbers.

def inject_to_list(numbers, inject):
    injected_list = []
    for i in range(len(numbers)):
        injected_list.append(numbers[i])
        if i == len(numbers)-1:
            break
        else:
            injected_list.append(inject)
    return injected_list

list1, seperator1 = [12, -7, 3, -89, 14, 88, -78, -1, 2, 7], 6 # [12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]
list2, seperator2 = [1, 2, 3, 4, 5, 6], 9 # [1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]

print(inject_to_list(list1, seperator1))
print(inject_to_list(list2, seperator2))