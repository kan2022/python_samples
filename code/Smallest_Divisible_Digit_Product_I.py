# 06/08/2026
# Link: https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        p = 1
        for i in str(n):
            p = p * int(i)
        while p % t != 0:
            n += 1
            p = 1
            for i in str(n):
                p = p * int(i)
        return n