# 25/10/2024
# Link: https://leetcode.com/problems/remove-element/

import time


def remove_element(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


try:
    print("Enter a list of numbers seperated by spaces:")
    list_of_numbers = list(map(int, input().split()))
    print("Now enter a value that equals to one of the numbers you have just input:")
    value = int(input())

    f = remove_element(list_of_numbers, value)

    print("There are {} numbers if we remove are the {}'s:".format(f, value))
    print(list_of_numbers[:f])

except ValueError:
    print("Bad input, exiting programme...")
    j = 0
    while j <= 3:
        time.sleep(2)
        print("...")
        j += 1
    exit()

