# 12/08/26
# Link: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] + 1
        count = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == count+1:
                count = nums[i]
            else:
                result = sum(nums[:i])
                while result in nums:
                    result += 1
                return result
        return sum(nums)