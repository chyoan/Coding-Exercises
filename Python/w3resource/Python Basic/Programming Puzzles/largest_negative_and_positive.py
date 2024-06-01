# Write a Python program to find the largest negative and smallest positive numbers (or 0 if none).

def find_largest(lst):
    lst.sort()

    negative_nums = [num for num in lst if num < 0]
    positive_nums = [num for num in lst if num > 0]
    
    largest_negative = max(negative_nums) if negative_nums else 0
    smallest_postive = min(positive_nums) if positive_nums else 0

    return [largest_negative, smallest_postive]

list1 = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18] # [-6, 2]
list2 = [-1, -2, -3, -4] # [-1, 0]
list3 = [1, 2, 3, 4] # [0, 1]
list4 = [] # [0, 0]

print(find_largest(list1))
print(find_largest(list2))
print(find_largest(list3))
print(find_largest(list4))