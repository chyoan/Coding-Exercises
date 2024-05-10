# Write a Python program to find the longest string in a given list of strings.

lst = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

longest = ""
for word in lst:
    if len(word) > len(longest):
        longest = word
        
print(longest)
