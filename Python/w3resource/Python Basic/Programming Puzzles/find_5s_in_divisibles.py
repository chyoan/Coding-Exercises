# Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.
# (and the index where the 5 is found)
# Note: the 2nd comment is not in the original problem statement, i just added it because the sample output made me confused.

def find_5s(num):
    all_5s = []
    for i in range(num):
        if "5" in str(i) and (i % 9 == 0 or i % 15 == 0):
            all_5s.append([i, str(i).index('5')])
    return all_5s

n1 = 50 # [[15, 1], [45, 1]]
n2 = 65 # [[15, 1], [45, 1], [54, 0]]
n3 = 75 # [[15, 1], [45, 1], [54, 0]]
n4 = 85 # [[15, 1], [45, 1], [54, 0], [75, 1]]
n5 = 150 # [[15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]

print(find_5s(n1))
print(find_5s(n2))
print(find_5s(n3))
print(find_5s(n4))
print(find_5s(n5))