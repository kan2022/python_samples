# 25/02/25#
# Link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

def numOfSubarrays(ar):
    if not 1 <= len(ar) <= 105:
        return ar
    for i in range(len(ar)):
        if not 1 <= ar[i] <= 100:
            return ar
    a = all(num % 2 == 0 for num in ar)
    if a:
        return 0
    solution = 0
    for i in range(len(ar)):
        for j in range(i, len(ar)):
            if sum(ar[i:j+1]) % 2 == 1:
                solution += 1
    return solution


arr = list(map(int, input('Enter numbers separated by spaces: ').split()))
print(numOfSubarrays(arr))

