# 22/04/25
# Link: https://leetcode.com/problems/can-place-flowers/

def canPlaceFlowers(lst, n):
    count = 0
    i = 0
    while i < len(lst):
        if lst[i] == 0 and (i == 0 or lst[i - 1] == 0) and (i == len(lst) - 1 or lst[i + 1] == 0):
            lst[i] = 1
            count += 1
            if count >= n:
                return True
        i += 1
    return count >= n


flowerbed = list(map(int, input("Enter a list of number separated by spaces: ").split()))
num = int(input("Enter a number: "))
print(canPlaceFlowers(flowerbed, num))
