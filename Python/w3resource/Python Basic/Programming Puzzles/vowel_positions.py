# Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.

def find_position(string):
    upper_even_vowels = []
    for i in range(len(string)):
        if string[i] in 'AEIOU' and i % 2 == 0:
            upper_even_vowels.append(i)
    
    return upper_even_vowels

given_string1 = "w3rEsOUrcE"
given_string2 = "AEIOUYW"

print(find_position(given_string1))
print(find_position(given_string2))

