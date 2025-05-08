# 08/05/2025
# Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/

def dominoPairs(dom):
    if not 1 <= len(dominoes) <= 4 * 104:
        return None
    for i in dom:
        if not len(i) == 2:
            return None
        for j in i:
            if not 1 <= dominoes[i][j] <= 9:
                return None
    result = {}
    for i in dom:
        a = tuple(sorted(i))
        if a in result:
            result[a] += 1
        else:
            result[a] = 0
    n = 0
    for i in result.values():
        n += (i*(i+1)) // 2
    return n


i = int(input("Enter the number of domino pair you want"))
dominoes = []
for j in range(i):
    dominoes.append(list(map(int, input(f"Enter domino pair {j + 1} separated by spaces: ").split())))
print(dominoPairs(dominoes))
