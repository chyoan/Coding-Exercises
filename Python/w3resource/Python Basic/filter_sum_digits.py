# Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.

def filter_sum(lst):
    str_list = [str(n) for n in lst]
    sum_greater_than_zero = []
    for num in str_list:
        digits_sum = 0
        i = 0
        while i < len(num):
            if num[i] == '-':
                digits_sum -= int(num[i+1])
                i += 2
            else:
                digits_sum += int(num[i])
                i += 1
        if digits_sum > 0:
            sum_greater_than_zero.append(int(num))
    return sum_greater_than_zero

list1 = [11, -6, -103, -200]
list2 = [1, 7, -4, 4, -9, 2]
list3 = [10, -11, -71, -13, 14, -32]

print(filter_sum(list1))
print(filter_sum(list2))
print(filter_sum(list3))
