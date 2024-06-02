# A string is happy if every three consecutive characters are distinct. 
# Write a Python program to find two indices associated with a given string being unhappy.

def find_indices(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return [i, i+1]
    return None

string1 = "Python" # None 
string2 = "Unhappy" # [4, 5]
string3 = "Find" # None
string4 = "Street" # [3, 4]

print(find_indices(string1))
print(find_indices(string2))
print(find_indices(string3))
print(find_indices(string4))