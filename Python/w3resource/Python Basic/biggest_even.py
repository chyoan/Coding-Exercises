# Write a Python program to find the biggest even number between two numbers inclusive.

def find_biggest_even(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num2, num1-1, -1):
        if i % 2 == 0:
            return i
        
# Input: m = 12 n = 51
# Output: 50
# Input: m = 1 n = 79
# Output: 78
# Input: m = 47 n = 53
# Output: 52
# Input: m = 100 n = 200
# Output: 200

print(find_biggest_even(12, 51))
print(find_biggest_even(1, 79))
print(find_biggest_even(47, 53))
print(find_biggest_even(100, 200))