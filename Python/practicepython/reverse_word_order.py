# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string: My name is Michele
# Then I would see the string: Michele is name My

def reverse_word_order(text):
    return ' '.join(reversed(text.split()))

def get_input(prompt):
    while True:
        word = input(prompt)
        if len(word.strip()) == 0:
            print("Pleae enter something.")
        else:
            return word
       
string = get_input("Enter a string: ")

print(reverse_word_order(string))