# Write a Python program to find a list of integers with exactly two occurrences of nineteen 
# and at least three occurrences of five. Return True otherwise False.

def checker(l):
    if l.count(19) == 2 and l.count(5) >= 3:
        return True
    return False

lst = [19, 19, 5, 5, 5, 5, 5]

print(lst)
print(checker(lst))
