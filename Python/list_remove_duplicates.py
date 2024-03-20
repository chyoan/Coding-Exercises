# Write a program (function!) that takes a list and returns a new list 
# that contains all the elements of the first list minus all the duplicates.

def remove_duplicates(lst):
    new_list = []
    [new_list.append(i) for i in lst if i not in new_list]
    return new_list

a = [1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 1, 3, 4]

print(remove_duplicates(a))