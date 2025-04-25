# 24/04/2025
# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def removeDuplicates(s):
    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            s = s[:i - 1] + s[i + 1:]
            if not i == 1:
                i -= 1
        else:
            i += 1
    return s


string = input("Enter a string: ")
print(removeDuplicates(string))
