# Write a Python program to find the h-index, the largest positive number h such that h occurs in the sequence at least h times. 
# If there is no such positive number return h = -1.

def find_number(lst):
    lst.sort(reverse=True)
    for num in lst:
        if lst.count(num) >= num:
            return num
    return -1

list1 = [1, 2, 2, 3, 3, 4, 4, 4, 4] # 4
list2 = [1, 2, 2, 3, 4, 5, 6] # 2
list3 = [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5] # 5

print(find_number(list1))
print(find_number(list2))
print(find_number(list3))