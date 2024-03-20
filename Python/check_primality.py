# Ask the user for a number and determine whether the number is prime or not.

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 1:
                print("Number must be greater than 1.")
            else:
                return value
        except ValueError:
            print("Please enter a number only.")

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime number."
    return f"{num} is a prime number."  
        
number = get_valid_integer("Enter a number: ")

print(is_prime(number))