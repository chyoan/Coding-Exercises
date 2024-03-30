# Write a Python program to create a string consisting of non-negative integers up to n inclusive.

n = 15

string = ""
for i in range(n+1):
    string += str(i) + ' '
    
print(string)
