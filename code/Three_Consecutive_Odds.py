# 11/05/2025
# Link: https://leetcode.com/problems/three-consecutive-odds/

def threeOdds(arr):
    if not 1 <= len(arr) <= 1000:
        return None
    for i in arr:
        if not 1 <= i <= 1000:
            return None
    a = False
    b = False
    c = False
    odd_numbers = [1, 3, 5, 7, 9]
    for i in arr:
        j = i % 10
        if not a:
            if j in odd_numbers:
                a = True
            continue
        if not b:
            if j in odd_numbers:
                b = True
                continue
            a = False
            continue
        if not c:
            if j not in odd_numbers:
                b = False
                a = False
                continue
        return True
    return False


array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
print(threeOdds(array))
