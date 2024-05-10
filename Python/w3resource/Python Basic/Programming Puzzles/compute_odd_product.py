# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.

def compute_odd_product(number):
    product = 1
    numbers = [int(n) for n in str(number)]
    for num in numbers:
        if num % 2 != 0:
            product *= num
    if all(num % 2 == 0 for num in numbers):
        product = 0
    return product
  
number1 = 123456789
number2 = 2468
number3 = 13579

print(compute_odd_product(number1))
print(compute_odd_product(number2))
print(compute_odd_product(number3))