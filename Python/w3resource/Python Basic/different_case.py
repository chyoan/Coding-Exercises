# Write a Python program to find the dictionary key whose case is different from all other keys.

def find_dict_key(dictionary):
    upper_keys = []
    lower_keys = []
    for key in dictionary.keys():
        if key.isupper():
            upper_keys.append(key)
        else:
            lower_keys.append(key)

    if len(upper_keys) == 1:
        return upper_keys[0]
    elif len(lower_keys) == 1:
        return lower_keys[0]
    else:
        return None

dict1 = {'red': '', 'GREEN': '', 'blue': 'orange'} # GREEN
dict2 = {'RED': '', 'GREEN': '', 'orange': '#125GD'} # orange
 
print(find_dict_key(dict1))
print(find_dict_key(dict2))
