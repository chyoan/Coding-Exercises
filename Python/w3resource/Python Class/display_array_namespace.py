# Write a Python program to import a built-in array module and display the namespace of the said module.

import array
for namespace in array.__dict__:
    print(namespace)