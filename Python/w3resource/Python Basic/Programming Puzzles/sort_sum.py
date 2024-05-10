# Write a Python program to sort the numbers in a given list by the sum of their digits.

def sort_sum(lst):
    str_numbers = [str(n) for n in lst]
    digits_sum = []
    for num in str_numbers:
        digit_sum = 0
        for digit in num:
            digit_sum += int(digit)           
        digits_sum.append((digit_sum, int(num)))
    digits_sum.sort()
    sorted_num = [n for _, n in digits_sum]
    return sorted_num

list1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list2 = [23, 2, 9, 34, 8, 9, 10, 74]

print(sort_sum(list1))
print(sort_sum(list2))
