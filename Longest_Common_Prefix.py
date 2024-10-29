# Date: 06/10/2024
# Link leetcode: https://leetcode.com/problems/longest-common-prefix/

def prefix_verifier(strList):
    if not strList:
        return ""

    list_len = len(strList)
    result = ""
    for j in range(len(strList[0])):
        char = strList[0][j]
        for i in range(1, list_len):
            if j >= len(strList[i]) or strList[i][j] != char:
                return result
        result += char

    return result


print("Input a list of strings separated by spaces:")
list_strings = input().lower().split()
print(prefix_verifier(list_strings))
