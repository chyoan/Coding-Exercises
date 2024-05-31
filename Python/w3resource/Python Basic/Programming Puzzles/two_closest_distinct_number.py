# Write a Python program to find the two closest distinct numbers in a given list of numbers.

def find_closest(numbers):
    numbers = list((set(numbers)))
    numbers.sort()
    lowest_difference = float('inf')
    for i in range(len(numbers)-1):
        difference = abs(numbers[i] - numbers[i+1])
        if difference < lowest_difference:
            lowest_difference = difference
            pair = [numbers[i], numbers[i+1]]
    return pair

list1 = [1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
list2 = [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]

print(find_closest(list1))
print(find_closest(list2))