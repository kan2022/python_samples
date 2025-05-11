# 11/05/2025
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/

def guess(n):
    if n < pick:
        return 1  # Guess too low
    elif n > pick:
        return -1  # Guess too high
    else:
        return 0  # Correct guess


def guessNumber(n):
    if not 1 <= n <= 2**31 - 1:
        return None

    if n == 2:
        if guess(1) == 0:
            return 1
        return 2
    i = (n + 1) // 2
    low = 1
    high = n
    while low <= high:
        a = guess(i)
        if a == 0:
            return i
        elif a < 0:
            high = i - 1
        else:
            low = i + 1
        i = (low + high) // 2
    return -1


n = int(input("Enter the number: "))
pick = int(input("Enter the pick number: "))
if not 1 < pick < n:
    print()
else:
    print("The number is: ", guessNumber(n))
