# 15/04/2025
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies, extra):
    if not 2 <= len(candies) <= 100 or 1 <= extraCandies <= 50:
        return ""
    for i in candies:
        if not 1 <= i <= 100:
            return ""
    result = []
    max_can = max(candies)
    for i in candies:
        if i + extra >= max_can:
            result.append(True)
        else:
            result.append(False)
    return result


candiesList = list(map(int, input("Enter a list of candies separated by spaces: ").split()))
extraCandies = int(input("Enter the number of extra candy."))
print(kidsWithCandies(candiesList, extraCandies))
