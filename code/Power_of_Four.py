# 24/02/25
# Link: https://leetcode.com/problems/power-of-four/

def isPowerOfFour(n):
    if not -231 <= n <= 231-1:
        return n
    if not n > 0:
        return False
    a = 0
    while 4 ** a <= n:
        if n == 4 ** a:
            return True
        a += 1
    return False


num = int(input("Enter a number: "))
print(isPowerOfFour(num))
