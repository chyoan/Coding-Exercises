# Write a Python program to find the largest k numbers from a given list of numbers.

def find_largest(lst, value):
    lst.sort(reverse=True)
    largest = lst[:value]
    return largest

lst = [1, 2, 3, 4, 5, 5, 3, 6, 2]

print(find_largest(lst, 1))
print(find_largest(lst, 2))
print(find_largest(lst, 3))
print(find_largest(lst, 4))