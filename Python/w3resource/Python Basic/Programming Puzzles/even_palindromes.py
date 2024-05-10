# Write a Python program to find all even palindromes up to n.

def find_even_palindromes(number):
    even_palindromes = []
    for num in range(number+1):
        if str(num) == str(num)[::-1] and num % 2 == 0:
            even_palindromes.append(num)
    return even_palindromes

print(find_even_palindromes(50))
print(find_even_palindromes(100))
print(find_even_palindromes(500))
print(find_even_palindromes(2000)) 