# You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.
# As the writer of this program, you will have to choose how your program will strategically guess. 

import random

lower = 0
upper = 100
guess_number = 0

number = random.randint(lower, upper) # Instead of user thinking of a number everytime, the program will generate a random number instead 
print(f"Number to guess: {number}")

choice = ['too high', 'too low', 'correct']

while lower < upper :
    mid = (lower + upper) // 2
    print(f"Guess: {mid}")
    
    user = input("Is the guess too high, too low, or correct? ").lower()
    if user not in choice:
        print("Invalid input.")
        continue
    
    if user == 'too low':
        lower = mid + 1
        guess_number += 1
    elif user == 'too high':
        upper = mid
        guess_number += 1
    else:
        guess_number += 1
        break

print(f"\nNumber of guesses: {guess_number}")
