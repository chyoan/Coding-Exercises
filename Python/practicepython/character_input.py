# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)

def get_valid_age(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Your age must be positive.")
            else:
                return num
        except ValueError:
            print("Please enter a valid age.")

name = input("Enter your name: ")
age = get_valid_age("Enter your age: ")
                
year = 2024 - age + 100

print(f"Hello {name}! You will turn 100 years old at year {year}")
