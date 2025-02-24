# 24/02/25
# Link: https://leetcode.com/problems/two-sum/

def twoSum(n, tar):
    if not 2 <= len(n) <= 104:
        return n
    if not -109 <= tar <= 109:
        return n
    for i in n:
        if not -109 <= i <= 109:
            return n
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == tar:
                return [i, j]


num = list(map(int, input('Enter numbers separated by spaces: ').split()))
target = int(input('Enter target: '))
print(twoSum(num, target))

