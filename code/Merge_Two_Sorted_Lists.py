# 05/10/2024
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

def two_to_one_list(x):
    for h in range(len(x)):
        prev_numb_in_list = 0
        for i in range(len(x)):
            if x[i] < prev_numb_in_list:
                x[i], x[i - 1] = x[i - 1], x[i]
            prev_numb_in_list = x[i]
    return x

print("Enter two list of numbers separated by spaces:")
try:
    list1 = input("list1: ")
    list2 = input("list2: ")

    list1 = list(map(int, list1.split()))
    list2 = list(map(int, list2.split()))

    merged_list = list1 + list2

    print(two_to_one_list(merged_list))
except ValueError:
    print("Please enter a list of numbers separated by spaces.")
    exit(1)
