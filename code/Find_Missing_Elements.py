# 14/08/26
# Link: https://leetcode.com/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = nums[0]
        b = nums[0]
        for i in nums:
            if i > b:
                b = i
            elif i < s:
                s = i
        result = []
        for j in range(s, b):
            if j not in nums:
                result.append(j)

        return result