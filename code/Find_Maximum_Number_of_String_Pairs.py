# 12/08/2026
# Link: https://leetcode.com/problems/maximum-number-of-string-pairs/

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        tracker = []
        pairs = 0
        for i in words:
            j = i[1]+i[0]
            if j in tracker:
                tracker.remove(j)
                pairs += 1
            else:
                tracker.append(i)
        return pairs
