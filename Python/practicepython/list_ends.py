# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def list_ends(lst):
    end = [lst[0], lst[-1]]
    return end

print(list_ends(a))