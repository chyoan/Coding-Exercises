# Write a Python program to find the indices of three numbers that sum to 0 in a given list of numbers.

# Note: this func only returns the last set of indices as per the expected ouput.
# i can make it so that it only returns the first instance but im just following the output so ye 
# (also haven't taken dsa yet atp so pretty much a bad bruteforce solu)

def find_indices(numbers):
    indices = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                total = numbers[i] + numbers[j] + numbers[k]
                if total == 0:
                    indices = [i,j,k]
    return indices

list1 = [12, -7, 3, -89, 14, 4, -78, -1, 2, 7] # [1, 2, 5]  
list2 = [1, 2, 3, 4, 5, 6, -7] # [2, 3, 6]

print(find_indices(list1))
print(find_indices(list2))