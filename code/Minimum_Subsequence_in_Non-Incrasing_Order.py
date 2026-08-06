# 06/08/2026
# Link: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        count = nums[0]
        a = 0
        for i in nums[1:]:
            a += i
        if count > a:
            return [count]
        for i in range(1, len(nums)):
            count += nums[i]
            track = 0
            boo = False
            for j in nums[i+1:]:
                track += j
                boo = True
            if count > track and boo:
                return nums[:i+1]
        return nums
