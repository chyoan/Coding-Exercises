# Write a Python program to remove duplicates from a list of integers, preserving order.

def remove_duplicates(lst):
    new_list = []
    for integer in lst:
        if integer not in new_list:
            new_list.append(integer)
    return new_list

print(remove_duplicates([1, 3, 4, 10, 4, 1, 43])) # [1, 3, 4, 10, 43]
print(remove_duplicates([10, 11, 13, 23, 11, 25, 23, 76, 99])) # [10, 11, 13, 23, 25, 76, 99]