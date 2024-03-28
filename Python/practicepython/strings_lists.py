# Ask the user for a string and print out whether this string is a palindrome or not. 
# A palindrome is a string that reads the same forwards and backwards.

text = input("Enter a string: ")

processed_text = text.replace(' ','').lower() # This doesn't count special characters as that would require us to import the re module

if processed_text == processed_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
