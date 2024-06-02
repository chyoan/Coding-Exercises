# Write a Python program to calculate the average of the numbers a through b (b not included) rounded to the nearest integer, in binary (or -1 if there are no such numbers).

def calculate_average(a, b):
    if a >= b:
        return -1
    total = sum(range(a, b))
    count = b - a
    return bin(round(total/count))

print(calculate_average(4, 7)) # 0b101
print(calculate_average(11 , 19)) # 0b1110