# 17/02/25
# Link: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/


def sum_k_bits_indices(n, k):
    if 1 <= len(nums) <= 1000 and 0 <= k <= 10:
        a = True
        for i in range(0, len(nums)):
            if not 1 <= nums[i] <= 10**5:
                a = False
                break
        if a:
            nSetBits = []
            for i in range(0, len(nums)):
                nBits = 0
                while i > 0:
                    if i % 2 == 1:
                        nBits += 1
                    i //= 2
                nSetBits.append(nBits)
            result = 0
            for i in range(len(nums)):
                if nSetBits[i] == k:
                    result += nums[i]
            return result
    return nums


nums = list(map(int, input("Input a 0-indexed list of numbers separated by spaces: ").split()))
k = int(input("Input the number of k: "))
print(sum_k_bits_indices(nums, k))

