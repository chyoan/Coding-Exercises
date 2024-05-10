# Write a Python program to create a new string by taking a string, and word by word rearranging its characters in ASCII order.

def rearrange_order(string):
    if ' ' in string:
        string = string.split()
        new_string = []
        for word in string:
            new_string.append(''.join(sorted(word)))
        return ' '.join(new_string)
    else:
        return ''.join(sorted(string))

string1 = "Ascii character table" # Aciis aaccehrrt abelt
string2 = "maltos won" # almost now

print(rearrange_order(string1))
print(rearrange_order(string2))