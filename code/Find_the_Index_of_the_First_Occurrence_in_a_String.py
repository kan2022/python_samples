# 26/10/2024
# Link: https://leetcode.com/problems/implement-strstr/

def find_first_index(str, n):
    if len(n) > len(str):
        return -1

    k = 0

    for i in range(len(str)):
        if str[i] == n[k]:
            k += 1
            if k-len(n) == 0:
                if str[i+1-len(n):i+1] == n:
                    return i+1-len(n)

        else:
            k = 0
            if str[i] == n[k]:
                k += 1

    k = 0
    return k-1


print("Enter a string")
string = input()

print("Enter a needle in the previous word")
needle = input()

try:
    index = find_first_index(string, needle)
    print(index)
except IndexError or ValueError:
    print("Index not found")

