# Write a Python program to determine which triples sum to zero from a given list of lists.

def check_zero_sum(lst):
    results = []
    for i in lst:
        if sum(i) == 0:
            results.append(True)
        else:
            results.append(False)
    return results
            
given1 = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
given2 = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]

print(check_zero_sum(given1))
print(check_zero_sum(given2))