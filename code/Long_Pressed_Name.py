# 25/02/25
# Link: https://leetcode.com/problems/long-pressed-name/

def verification(na, ty):
    if not 1 <= len(na) <= 1000 or not 1 <= len(ty) <= 1000:
        return na, ty
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in na:
        if i not in letters:
            return na, ty
    for i in ty:
        if i not in letters:
            return na, ty
    t = 0
    for i in range(len(ty)):
        if t < len(na) and ty[i] == na[t]:
            t += 1
        elif t == 0 or ty[i] != na[t - 1]:
            return False
    return t == len(na)


name = input("Enter the name: ")
typed = input("Enter the typed: ")
print(verification(name, typed))

