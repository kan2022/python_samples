# 30/10/2024, tomorrow is Halloween!
# Link: https://leetcode.com/problems/climbing-stairs/

def count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    m = 1
    s = 2
    result = 0
    k = 1
    while k <= n - 2:
        result = s + m
        m = s
        s = result
        k += 1

    return result


print("Input a number of stairs:")
stairs_number = int(input())
if stairs_number <= 0:
    i = 0
    while i <= 1:
        print("Input a number of stairs > 0:")
        stairs_number = int(input())
print("There are {} numbers of ways to get to the stair number {}" .format(count(stairs_number), stairs_number))

