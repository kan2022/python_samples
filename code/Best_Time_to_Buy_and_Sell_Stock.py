# 31/10/2024, Halloween!
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maximum_profit_finder(p):
    profit_list = []

    for k in range(0, len(p)):
        for m in range(k+1, len(p)):
            if p[m] > p[k]:
                profit_list.append(p[m]-p[k])

    for d in range(len(profit_list)):
        for f in range(d+1, len(profit_list)):
            if profit_list[f] > profit_list[d]:
                profit_list[d], profit_list[f] = profit_list[f], profit_list[d]

    if 0 <= profit_list[0] <= 10 ** 4:
        return "Profit too high, error..."

    return profit_list[0]


a = 0
while a <= 3:
    print("Enter an array of prices separated by spaces:")
    prices = list(map(int, input().split()))
    if 1 <= len(prices) <= 10 ** 5:
        print(maximum_profit_finder(prices))
        a = 4
    else:
        print("The length of the array must be between 1 and 105.")
        a += 1

