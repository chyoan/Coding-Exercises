# Write a Python program to find the index of the matching parentheses for each character in a given string.

def find_index_of_matching_parenthesis(string):
    stack = []
    matching_parenthesis_index = [None] * len(string)
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                matching_parenthesis_index[stack[-1]] = i
                matching_parenthesis_index[i] = stack.pop()
    return matching_parenthesis_index

string1 = "()(())" # [1, 0, 5, 4, 3, 2]
string2 = "()()()" # [1, 0, 3, 2, 5, 4]
string3 = "((()))" # [5, 4, 3, 2, 1, 0]

print(find_index_of_matching_parenthesis(string1))
print(find_index_of_matching_parenthesis(string2))
print(find_index_of_matching_parenthesis(string3))

# Don't know stack data structure yet so i just partially copied the solution and studied what stack is