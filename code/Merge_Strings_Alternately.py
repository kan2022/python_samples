# 26/02/25
# Link: https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(wo1, wo2):
    if not 1 <= len(wo1) <= 100 or not 1 <= len(wo2) <= 100:
        return wo1, wo2
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(wo1)):
        if wo1[i] not in letters:
            return wo1, wo2
    for i in range(len(wo2)):
        if wo2[i] not in letters:
            return wo1, wo2
    result = wo1[0]
    t = 1
    for t2 in range(len(wo2)):
        if t < len(wo1):
            result += wo2[t2] + wo1[t]
        else:
            result += wo2[t2]
        t += 1
    if len(result) != len(wo1 + wo2):
        result += wo1[t:]
    return result


word1 = input("Enter 1st word: ")
word2 = input("Enter 2nd word: ")
print(mergeAlternately(word1, word2))

