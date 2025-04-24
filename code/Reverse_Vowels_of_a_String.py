# 24/04/2025
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

def reverseVowels(s):
    if not 1 <= len(s) <= 3 * 105:
        return None
    ascii_printable = [chr(i) for i in range(32, 127)]
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    lst = []
    for char in s:
        if char not in ascii_printable:
            return None
        if char in vowels:
            lst.append(char)
    result = ""
    for char in s:
        if char in vowels:
            result += lst[-1]
            lst.pop(-1)
        else:
            result += char
    return result


string = input("Enter a string: ")
print(reverseVowels(string))
