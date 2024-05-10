# Write a Python program to find even-length words from a given list of words and sort them by length.

def even_length_sort(lst):
    lst.sort()
    even_words = []
    for item in lst:
        if len(item) % 2 == 0:
            even_words.append(item)
    even_words.sort(key=len)
    return even_words

list1 = ['Red', 'Black', 'White', 'Green', 'Pink', 'Orange'] # ['Pink', 'Orange']
list2 = ['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!'] # ['!!', 'bird', 'that', 'worm', 'Absurd']

print(even_length_sort(list1))
print(even_length_sort(list2))
