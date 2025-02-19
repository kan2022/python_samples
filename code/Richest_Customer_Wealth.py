# 18/02/2025
# Link: https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(acc):
    if len(acc) >= 1:
        a = True
        for i in range(len(acc)):
            for j in range(len(acc[i])):
                if not 1 <= acc[i][j] <= 100:
                    a = False
                    break
        if a:
            result = 0
            for i in range(len(acc)):
                if result < sum(acc[i]):
                    result = sum(acc[i])
            return result
    return acc


accounts = [list(map(int, row.split())) for row in input().split(',')]
print(maximumWealth(accounts))

