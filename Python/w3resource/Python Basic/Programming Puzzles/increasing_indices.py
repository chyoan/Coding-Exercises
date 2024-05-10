# Write a Python program to find the indices of two entries that show that the list is not in increasing order. 
# If there are no violations (they are increasing), return an empty list.

def find_indices(numbers):
    if all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)):
        return []

    for i in range(len(numbers)-1):
        if not numbers[i] <= numbers[i+1]:
            return [i, i+1]

nums1 = [1, 2, 3, 0, 4, 5, 6] # [2, 3]
nums2 = [1, 2, 3, 4, 5, 6] # []
nums3 = [1, 2, 3, 4, 6, 5, 7] # [4, 5]
nums4 = [-3, -2, -3, 0, 2, 3, 4] # [1, 2]

print(find_indices(nums1))
print(find_indices(nums2))
print(find_indices(nums3))
print(find_indices(nums4))