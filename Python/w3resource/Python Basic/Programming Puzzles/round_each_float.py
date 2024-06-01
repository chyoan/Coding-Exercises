# Write a Python program to round each float in a given list of numbers up to the next integer and return the running total of the integer squares.
import math

def round_floats(numbers):
    rounds = []
    total = 0
    for num in numbers:
        total += math.ceil(num) ** 2
        rounds.append(total)
    return rounds

numbers1 = [2.6, 3.5, 6.7, 2.3, 5.6] # [9, 25, 74, 83, 119]
numbers2 = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0] # [91204, 252808, 253337, 183714223444221, 183714327525025, 283714327525025]

print(round_floats(numbers1))
print(round_floats(numbers2))