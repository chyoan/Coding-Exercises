# Write a Python program to find the largest integer divisor of a number n that is less than n.

def find_divisors(num):
    divisors = []
    for n in range(1, num):
        if num % n == 0:
            divisors.append(n)
    return max(divisors)

print(find_divisors(18))
print(find_divisors(100))
print(find_divisors(102))
print(find_divisors(500))
print(find_divisors(1000))
print(find_divisors(6500))
