# Write a Python program to find a substring in a given string that contains a vowel between two consonants.

def find_substring(string):
    for i in range(1, len(string)-1):
        if (string[i].isalpha() and string[i] in 'aeiouAEIOU') and (
        (string[i-1].isalpha() and string[i-1] not in 'aeiouAEIOU') and (string[i+1].isalpha() and string[i+1] not in 'aeiouAEIOU')):
            return string[i-1]+string[i]+string[i+1]
    return None

string1 = "Hello" # Hel
string2 = "Sandwhich" # San
string3 = "Python" # hon

print(find_substring(string1))
print(find_substring(string2))
print(find_substring(string3))