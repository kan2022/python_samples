'''def prefix_verifier(strList):
    list_len = len(strList)
    i = 0
    result = ""
    print(range(len(strList) - 1))
    for j in range(len(strList) - 1):
        while i < list_len - 1:
            if strList[i][j] != strList[i + 1][j]:
                result += strList[i][j]
                print(result)
                break
            i += 1
        i = 0'''

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

print("Input a list of strings seperated by spaces:")
list_strings = input().lower().split()
print(prefix_verifier(list_strings))
