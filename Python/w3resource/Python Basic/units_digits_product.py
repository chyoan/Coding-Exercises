# Write a Python program to find the product of the units digits in the numbers in a given list.

def find_product_units(lst):
    product = 1
    for num in lst:
        num = str(num)
        product *= int(num[-1])
    return product

print(find_product_units([12, 23])) # 6
print(find_product_units([12, 23, 43])) # 18
print(find_product_units([113, 234])) # 5
print(find_product_units([1002, 2005])) # 10

