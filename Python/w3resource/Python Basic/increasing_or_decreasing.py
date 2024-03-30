# Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.

number1 = [1, 2, 3, 4, 5]
number2 = [5, 4, 3, 2, 1]
number3 = [5, 1, 2, 4, 3]

def determine_direction(numbers):
    if all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)):
        return 'Increasing'
    elif all(numbers[i] >= numbers[i+1] for i in range(len(numbers)-1)):
        return 'Decreasing'
    else:
        return 'Not monotonic'

print(determine_direction(number1))
print(determine_direction(number2))
print(determine_direction(number3))
