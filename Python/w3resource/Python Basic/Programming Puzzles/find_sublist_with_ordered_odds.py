# Write a Python program to find the sublist of numbers from a given list of numbers with only odd digits in increasing order.

def find_sublist(numbers):
    return sorted([num for num in numbers if num % 2 == 1])

list1 = [1, 3, 79, 10, 4, 2, 39] # [1, 3, 39, 79]
list2 = [11, 31, 40, 68, 77, 93, 48, 1, 57] # [1, 11, 31, 57, 77, 93]
list3 = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1] # [-3, -1, 3, 9]

print(find_sublist(list1))
print(find_sublist(list2))
print(find_sublist(list3))