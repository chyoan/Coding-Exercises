# Write a Python program to reorder numbers from a given array in increasing/decreasing order based on whether the first plus last element is odd/even.
# Reorder numbers of a give array in increasing/decreasing order based on whether the first plus last element is odd/even.:

def rearrange_order(array):
    plus = array[0] + array[-1]
    if plus % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

array1 = [3, 7, 4] # [3, 4, 7]
array2 = [2, 7, 4] # [7, 4, 2]
array3 = [1, 5, 6, 7, 4, 2, 8] # [1, 2, 4, 5, 6, 7, 8]
array4 = [1, 5, 6, 7, 4, 2, 9] # [9, 7, 6, 5, 4, 2, 1]

print(rearrange_order(array1))
print(rearrange_order(array2))
print(rearrange_order(array3))
print(rearrange_order(array4))