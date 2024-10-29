# 05/10/2024
# Link: https://leetcode.com/problems/plus-one/

def plus_one(x):
    n = len(x)

    for i in range(n - 1, -1, -1):
        if x[i] < 9:
            x[i] = x[i] + 1
            return x
        x[i] = 0

    return [1] + x


print("Print a list of number seperated by space")

try:
    digits = list(map(int, input().split()))
    print(digits)
    print(plus_one(digits))
except ValueError:
    error = 0
    if error == 3:
        print("Too many errors, exiting program")
        exit()
    print("Print a list of number seperated by space")
