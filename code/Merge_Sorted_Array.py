# 30/10/2024, tomorrow is Halloween!
# Link: https://leetcode.com/problems/merge-sorted-array/
# Is there a difference between this and the Merge Two Sorted Lists exercise?

import time


def merge_array(arr1, m, arr2, n):
    k = 0
    for i in range(m, m + n):
        arr1[i] = arr2[k]
        k += 1

    for i in range(len(arr1)):
        for j in range(i + 1, len(arr1)):
            if arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]

    return arr1


try:
    print("Enter numbers separated by spaces in ascending order with some zeros at the end:")
    lst = list(map(int, input().split()))
    nums1 = [x for x in lst]

    print("Enter the number of numbers that you just inputted without counting the zeros:")
    m = int(input())

    print("Enter as many numbers as you written some zeros before :")
    lst = list(map(int, input().split()))
    nums2 = [x for x in lst]

    print("Enter the number of numbers that you just inputted:")
    n = int(input())

    print(merge_array(nums1, m, nums2, n))
except ValueError:
    g = 0
    print("Bad input, exiting code...")
    while g <= 3:
        print("...")
        time.sleep(2)
        g += 1
    exit()

