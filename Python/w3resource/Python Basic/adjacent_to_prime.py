# Write a Python program to find a list of all numbers that are adjacent to a prime number in the list, sorted without duplicates.

def adjacent_to_prime(nums):
    primes = []
    adjacent = []
    for num in nums:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    
    for i in range(len(nums)):
        num = nums[i]
        if num in primes:
            if i == 0:
                adjacent.append(nums[i+1])
            elif i == len(nums)-1:
                adjacent.append(nums[i-1])
            else:
                adjacent.append(nums[i-1])
                adjacent.append(nums[i+1])

    return sorted(list(set(adjacent)))
        
list1 = [2, 17, 16, 0, 6, 4, 5] # [2, 4, 16, 17]
list2 = [1, 2, 19, 16, 6, 4, 10] # [1, 2, 16, 19]
list3 = [1, 2, 3, 5, 1, 16, 7, 11, 4] # [1, 2, 3, 4, 5, 7, 11, 16]

print(adjacent_to_prime(list1))
print(adjacent_to_prime(list2))
print(adjacent_to_prime(list3))