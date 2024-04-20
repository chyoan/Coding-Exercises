# Write a Python program to find numbers that are greater than 10 and have odd first and last digits.

def find_number_and_filter(numbers):
    odd_digits_greater_than_ten = []
    for number in numbers:
        if number > 10:
            str_number = str(number)
            if int(str_number[0]) % 2 != 0 and int(str_number[-1]) % 2 != 0:
                odd_digits_greater_than_ten.append(int(str_number))
    return odd_digits_greater_than_ten

list1 = [1, 3, 79, 10, 4, 1, 39, 62] # [79, 39]
list2 = [11, 31, 77, 93, 48, 1, 57] # [11, 31, 77, 93, 57]

print(find_number_and_filter(list1))
print(find_number_and_filter(list2))