# Write a Python program to find the vowels from each of the original texts (y counts as a vowel at the end of the word) from a given list of strings.

def find_vowels(lst):
    vowels = 'AEIOUaeiou'
    vowels_list = []
    for item in lst:
        vowel = ''
        for ch in item:
            if ch in vowels:
                vowel += ch
        if len(item) > 0 and (item[-1] == 'y' or item[-1] == 'Y'):
            vowel += item[-1]
        vowels_list.append(vowel)
    return vowels_list

list1 = ['w3resource', 'Python', 'Java', 'C++'] # ['eoue', 'o', 'aa', '']
list2 = ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly'] # ['ay', 'auy', 'aeeay', 'aaey', 'aoeey']

print(find_vowels(list1))
print(find_vowels(list2))