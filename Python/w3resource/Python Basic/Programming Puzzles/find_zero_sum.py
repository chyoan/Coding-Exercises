# Write a Python program to find the number which when appended to the list makes the total 0.

def find_number(nums):
    total = sum(nums)
    return total * -1

array1 = [1, 2, 3, 4, 5] # -15
array2 = [-1, -2, -3, -4, 5] # 5
array3 = [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755] # 1316384

print(find_number(array1))
print(find_number(array2))
print(find_number(array3))