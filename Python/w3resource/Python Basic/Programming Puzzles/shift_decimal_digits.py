# Write a Python program to shift the decimal digits n places to the left, wrapping the extra digits around. 
# If the shift > the number of digits in n, reverse the string.

def shift_decimal_digits(number, shift):
    number = str(number)
    if shift > len(number):
        number = number[::-1]
    else:
        number = number[shift:] + number[:shift]
    return int(number)

print(shift_decimal_digits(12345, 1)) # 23451
print(shift_decimal_digits(12345, 2)) # 34512
print(shift_decimal_digits(12345, 3)) # 45123
print(shift_decimal_digits(12345, 5)) # 12345
print(shift_decimal_digits(12345, 6)) # 54321