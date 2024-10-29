# 28/10/2024
# Link: https://leetcode.com/problems/search-insert-position/

import time


def find_position(list, num):
    if num < list[0]:
        return 0
    
    try:
        for i in range(len(list)):
            if num == list[i]:
                return i
            elif num > list[i] and num < list[i+1]:
                return i+1
    except IndexError:
        return len(list)


try:
    print("Enter a list with numbers in ascending order and seperated by spaces")
    aList = list(map(int, input().split()))

    try:
        for v in range(len(aList)):
            if not aList[v] <= aList[v+1]:
                print("Bad Input, exiting programm...")

                p = 0
                while p <= 3:
                    print("...")
                    time.sleep(2)
                    p += 1
                exit()
    except IndexError:
        print("Enter a number")
        aNumber = int(input())

        index = find_position(aList, aNumber)
        print("The number {} is at position {}".format(aNumber, index))
except ValueError or IndexError:
    print("Error, exiting programme...")

    p = 0
    while p <= 3:
        print("...")
        time.sleep(2)
        p += 1
    
    exit()

