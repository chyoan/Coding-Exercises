# Write a Python program to find the string consisting of all the words whose lengths are prime numbers.

def find_word_with_prime_length(string):
    string = string.split()
    prime_words = []
    for word in string:
        if len(word) > 1:
            for i in range(2, int(len(word) ** 0.5) + 1):
                if len(word) % i == 0:
                    break
            else:
                prime_words.append(word)
    return ' '.join(prime_words)


string1 = "The quick brown fox jumps over the lazy dog." # The quick brown fox jumps the
string2 = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later." # Omicron Effect: Foreign Flights Won't On Dec 15,

print(find_word_with_prime_length(string1))
print(find_word_with_prime_length(string2))