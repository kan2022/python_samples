# 25/04/25
# Link: https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    i = 0
    try:
        for j in t:
            if s[i] == j:
                i += 1
    except:
        pass
    return i >= len(s)


string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
print(isSubsequence(string1, string2))
