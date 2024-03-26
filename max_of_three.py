# Implement a function that takes as input three variables, and returns the largest of the three. 
# Do this without using the Python max() function!

def get_max(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
        
print(get_max(3, 11, 5))
