# 05/08/2026
# Link: https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        result = 0
        for i in s:
            if i == '|':
                if count == 1:
                    count = 0
                else:
                    count = 1
            elif count == 0 and i == '*':
                result += 1
        return result
