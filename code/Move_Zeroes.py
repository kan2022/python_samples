# 25/04/25
# Link: https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    i = 0
    a = len(nums) - nums.count(0)
    while i != a:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i += 1


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(moveZeroes(numbers))
