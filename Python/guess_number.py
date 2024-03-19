#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

import random

number = random.randint(1, 9)

guess = int(input("Guess a number between 1 and 9: "))
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Exactly right!")

