# Write a Python program to find a string consisting of space-separated characters with given counts.

def generate_string(dictionary):
    string = ""
    for key, value in dictionary.items():
        string += key * value
    return ' '.join(string)

dict1 = {'f': 1, 'o': 2} # f o o
dict2 = {'a': 1, 'b': 1, 'c': 1} # a b c

print(generate_string(dict1))
print(generate_string(dict2))