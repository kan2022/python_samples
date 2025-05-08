# 08/05/2025
# Link: https://leetcode.com/problems/maximum-average-subarray-i/

def MaxAverage(nums, k):
    if not 1 <= k <= nums[n] <= 105:
        return None
    for i in range(len(nums)):
        if not -104 <= nums[i] <= 104:
            return None
    i = 1
    result = sum(nums[:k]) / k
    a = sum(nums[i:k])
    for j in range(k, len(nums)):
        a += nums[j]
        if a / k > result:
            result = a / k
        a -= nums[i]
        i += 1
    return result


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
k = int(input("Enter a number: "))
print(MaxAverage(numbers, k))
