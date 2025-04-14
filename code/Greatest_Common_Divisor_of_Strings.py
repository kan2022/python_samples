# 14/04/2025
# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/


def gcdOfStrings(str1, str2):
    if not 1 <= len(str1) <= 1000 or not 1 <= len(str2) <= 1000 or not str1.isupper() or not str2.isupper():
        return ""
    results = []
    longest_string = str1 if len(str1) > len(str2) else str2
    for i in range(1, len(longest_string) + 1):
        a = str2[:i]
        if str1[:i] == a and a * (len(str1) // len(a)) == str1 and a * (len(str2) // len(a)) == str2:
            results.append(a)
    print(results)
    return max(results, key=len) if results else ""


string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
print(gcdOfStrings(string1, string2))
