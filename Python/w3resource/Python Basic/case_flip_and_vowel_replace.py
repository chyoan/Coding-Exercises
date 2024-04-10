# Write a Python program to find strings that, when case is flipped, give a target where vowels are replaced by characters two later.

vowel_replacements = {'a':'c', 'A':'C',
                      'e':'g', 'E':'G',
                      'i':'k', 'I':'K',
                      'o':'q', 'O':'Q',
                      'u':'w', 'U':'W'}

def flip_replace(string):
    string = string.swapcase()
    for key, value in vowel_replacements.items():
        string = string.replace(key, value)
    return string

string1 = 'Python' # pYTHQN
string2 = 'aeiou' # CGKQW
string3 = 'Hello, world!' # hGLLQ, WQRLD!
string4 = 'AEIOU' # cgkqw

print(flip_replace(string1))
print(flip_replace(string2))
print(flip_replace(string3))
print(flip_replace(string4))