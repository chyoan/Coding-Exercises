# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

def get_valid_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a number.")
    
number = get_valid_number("Enter a number: ")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
