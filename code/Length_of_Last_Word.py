# 29/10/2024
# Link: https://leetcode.com/problems/length-of-last-word/

import time


def length_last_word(word):
    return len(word[-1])


i = 0
num_errors = 0
aList = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "}


while i <= 3:
    if i == 0:
        print("Enter a string:")
    else:
        print("Enter a correct string:")
    str = input()
    s = str.split()
    if 1 <= s.length <= 104:
        for m in str:
            if m not in aList:
                num_errors = 1
                break
        if num_errors == 0:
            print(length_last_word(s))
            exit()
    i += 1

print("Too much bad input, exiting programme...")
for k in range(3):
    time.sleep(3)
    print("...")
exit()




