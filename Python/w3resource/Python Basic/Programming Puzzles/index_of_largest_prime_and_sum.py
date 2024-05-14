# Write a Python program to find the index of the largest prime in the list and the sum of its digits.

def find_index_and_sum(lst):
    for number in sorted(lst, reverse=True):
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                break
        else:
            largest_prime = number
            index = lst.index(largest_prime)
            break
    
    total = 0
    for digit in str(largest_prime):
        total += int(digit)
    
    return [index, total]

list1 = [3, 7, 4] # [1, 7]
list2 = [3, 11, 7, 17, 19, 4] # [4, 10]
list3 = [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157] # [6, 7]

print(find_index_and_sum(list1))
print(find_index_and_sum(list2))
print(find_index_and_sum(list3))