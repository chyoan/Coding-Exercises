# Write a Python program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.

def swapcase_or_reversestring(lst):
    new_list = []
    for item in lst:
        if all(not item[i].isalpha() for i in range(len(item))):
            new_list.append(item[::-1])
        else:
            new_list.append(item.swapcase())
    return new_list

list1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique'] # ['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']
list2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White'] # ['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']
list3 = ['Hello', '!@#', '!@#$', '123#@!'] # ['hELLO', '#@!', '$#@!', '!@#321']

print(swapcase_or_reversestring(list1))
print(swapcase_or_reversestring(list2))
print(swapcase_or_reversestring(list3))