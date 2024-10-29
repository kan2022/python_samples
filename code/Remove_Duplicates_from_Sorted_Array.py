# 24/10/2024
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_duplicates(nums):
    h = 0

    for i in range(1, len(nums)):
        if nums[h] != nums[i]:
            h += 1
            nums[h] = nums[i]
            print(h)
        print(nums)

    return h + 1


j = 0
print("Enter a list of numbers separated by spaces like: 0 0 1 1 1 1 2 2 2 3 3 4 5 5 5 6 6 6 6 etc...")
numbers = list(map(int, input().split()))
n = remove_duplicates(numbers)
print("n = {}".format(n))
print(numbers[:n])

