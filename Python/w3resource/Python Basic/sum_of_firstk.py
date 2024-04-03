# Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits.

def find_sum(lst, value):
    sum = 0
    for num in lst[:value]:
        if abs(num) >= 100:
            sum += num
    return sum

list1 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
kvalue1 = 4
list2 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
kvalue2 = 6
list3 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
kvalue3 =5
list4 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
kvalue4 = 1

print(find_sum(list1, kvalue1))
print(find_sum(list2, kvalue2))
print(find_sum(list3, kvalue3))
print(find_sum(list4, kvalue4))
