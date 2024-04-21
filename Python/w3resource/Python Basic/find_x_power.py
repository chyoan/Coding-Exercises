# Write a Python program to find an integer exponent x such that a^x = n.

def find_x_power(a, n):
    x = 0
    while a ** x != n:
        if a ** x > n:
            return None
        x += 1
    return x
 
# a = 2 : n = 1024 ; x = 10
# a = 3 : n = 81 ; x = 4
# a = 3 : n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849 ; x = 170

print(find_x_power(2, 1024))
print(find_x_power(3, 81))
print(find_x_power(3, 1290070078170102666248196035845070394933441741644993085810116441344597492642263849))