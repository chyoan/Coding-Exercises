# Write a Python program to find the sum of the even elements that are at odd indices in a given list.

def find_sum_even_at_odd_indices(numbers):
    sum = 0
    for num in range(1, len(numbers), 2):
        if numbers[num] % 2 == 0:
            sum += numbers[num]
    return sum
    
list1 = [1, 2, 3, 4, 5, 6, 7] # 12
list2 = [1, 2, 8, 3, 9, 4] # 6

print(find_sum_even_at_odd_indices(list1))
print(find_sum_even_at_odd_indices(list2))