# Write a Python program that imports the abs() function using the builtins module, 
# displays the documentation of the abs() function and finds the absolute value of -155.

from builtins import abs

print(abs.__doc__)
print(abs(-155))