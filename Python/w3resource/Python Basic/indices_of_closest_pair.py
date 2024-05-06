# Write a Python program to find the indices of the closest pair from a list of numbers.

def find_indices(numbers):
    pair = []
    minimum_difference = float('inf')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if difference < minimum_difference:
                minimum_difference = difference
                pair = [i, j]
    return pair

list1 = [1, 7, 9, 2, 10] # [0, 3]
list2 = [1.1, 4.25, 0.79, 1.0, 4.23] # [4, 1]
list3 = [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2] # [2, 5]

print(find_indices(list1))
print(find_indices(list2))
print(find_indices(list3))