# Write a Python program to split a given string (s) into strings if there is a space in s, 
# otherwise split on commas if there is a comma, 
# otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).

s = "a b c d"
a = "a,b,c,d"
b = "ABCDabcd"

order = list("abcdefghijklmnopqrstuvwxyz")

def split_or_filter(s): 
    if ' ' in s:
        return s.split()
    elif ',' in s:
        return s.split(',')
    else:
        return [ch for ch in s if ch.islower() and order.index(ch) % 2 != 0]
          
print(split_or_filter(s))
print(split_or_filter(a))
print(split_or_filter(b))
