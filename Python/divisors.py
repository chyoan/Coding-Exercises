# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def get_valid_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number.")
    
number = get_valid_integer("Please enter a number: ")

divisors = []

# Use the abs function to also take account for negative numbers
# so instead of just (1, number+1), we can use this instead
for i in range(-abs(number), abs(number)+1): 
    try:
        if number % i == 0:
            divisors.append(i)
    except ZeroDivisionError:
        continue
        
print(f"The divisors are: {divisors}")
