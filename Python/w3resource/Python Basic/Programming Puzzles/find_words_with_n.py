# Write a Python program to find all words in a given string with n consonants.

def find_words(string, n):
    string = string.split()
    words = []
    for word in string:
        consonant = 0
        for ch in word:
            if ch.isalpha() and ch not in 'aeiouAEIOU':
                consonant += 1
        if consonant == n:
            words.append(word)
    return words
        
str1 = "this is our time"

print(find_words(str1, 3))
print(find_words(str1, 2))
print(find_words(str1, 1))