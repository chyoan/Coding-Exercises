# Write a Python program to find the set of distinct characters in a given string, ignoring case.

def find_distinct(string):
    string = list(set(string.lower()))
    return string

str1 = 'HELLO'
str2 = 'HelLo'
str3 = 'Ignoring case'

print(find_distinct(str1))
print(find_distinct(str2))
print(find_distinct(str3))