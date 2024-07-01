# Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.

def validate_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 0:
                raise ValueError
            return n
        except ValueError:
            print('Invalid input. Please enter a valid positive integer.')

def find_integer():
    even_digit = validate_input("Number of even digits: ")
    odd_digit = validate_input("Number of odd digits: ")

    return int('2'*even_digit + '3'*odd_digit)

print(find_integer())