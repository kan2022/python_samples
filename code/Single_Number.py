# 09/05/2025
# Link: https://leetcode.com/problems/single-number/

def singleNumber(nums):
    if not 1 <= len(nums) <= 3 * 104:
        return None
    for i in range(len(nums)):
        if not -3 * 104 <= nums[i] <= 3 * 104:
            return None
    tracker = set()
    for num in nums:
        if num in tracker:
            tracker.remove(num)
        else:
            tracker.add(num)
    result = {}
    for i in range(len(nums)):
        if nums[i] not in result:
            result[i] = 1
        else:
            result[i] += 1
    return min(result, key=result.get)


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(singleNumber(numbers))
