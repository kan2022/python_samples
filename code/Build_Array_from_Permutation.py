# 06/05/2025
# Link: https://leetcode.com/problems/build-array-from-permutation/

def buildArray(nums):
    if not 1 <= len(nums) <= 1000 or not 1 <= len(nums) <= 1000 or len(nums) != len(set(nums)):
        return None
    for i in range(len(nums)):
        if not 0 <= nums[i] < len(nums):
            return None
    result = []
    for i in range(len(nums)):
        result.append(nums[nums[i]])
    return result


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(buildArray(numbers))
