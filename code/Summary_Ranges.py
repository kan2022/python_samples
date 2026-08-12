# 10/08/26
# Link: https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        k = nums[0]
        result = []
        count = True
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if k != nums[i-1]:
                    result.append("{}->{}".format(k, nums[i-1]))
                else:
                    result.append("{}".format(k))
                k = nums[i]
            elif i == len(nums) - 1:
                result.append("{}->{}".format(k, nums[i]))
                count = False
        if count:
            result.append("{}".format(nums[-1]))
        return result
