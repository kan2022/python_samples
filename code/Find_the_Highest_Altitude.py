# 03/05/2025
# Link: https://leetcode.com/problems/find-the-highest-altitude/

def MaxAltitude(g):
    if not 1 <= len(g) <= 100:
        return None
    for i in g:
        if not -100 <= i <= 100:
            return None
    tracker = 0
    result = 0
    for i in g:
        tracker += i
        if result < tracker:
            result = tracker
    return result


gain = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print(MaxAltitude(gain))
