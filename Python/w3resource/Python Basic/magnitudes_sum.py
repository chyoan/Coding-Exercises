# Write a Python program to find the sum of the magnitudes of the elements in the array. 
# This sum should have a sign that is equal to the product of the signs of the entries.

def find_sum_magnitude(array):
    product = 1
    for element in array:
        if element < 0:
            product *= -1
    magnitude_sum = sum(abs(element) for element in array)
    return magnitude_sum * product

array1 = [1, 3, -2] # -6
array2 = [1, -3, 3] # -7
array3 = [10, 32, 3] # 45
array4 = [-25, -12, -23] # -60

print(find_sum_magnitude(array1))
print(find_sum_magnitude(array2))
print(find_sum_magnitude(array3))
print(find_sum_magnitude(array4))