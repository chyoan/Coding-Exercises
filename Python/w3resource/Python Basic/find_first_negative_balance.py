# Write a Python program to find the first negative balance from a given list of numbers that represent bank deposits and withdrawals.

def find_first_negative(lst):
    negative_balance = []
    for numbers in lst:
        balance = 0
        for number in numbers:
            balance += number
            if balance < 0:
                negative_balance.append(balance)
                break
        if balance > 0:
            negative_balance.append(None)
    return negative_balance

list1 = [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]] # [-81, -1]
list2 = [[1200, 100, -900], [100, 100, -2400]] # [None, -2200]

print(find_first_negative(list1))
print(find_first_negative(list2))