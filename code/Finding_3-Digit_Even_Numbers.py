# 01/06/2025
# Link: https://leetcode.com/problems/find-all-3-digit-even-numbers-that-can-be-formed-by-digits/

def EvenNumbers(dig):
    if not 3 <= len(dig) <= 100:
        return None
    for i in dig:
        if not 0 <= dig[i] <= 9:
            return False
    result = []
    for x in range(100, 999):
        if not x % 2 == 1:
            number = str(x)
            a = True
            dig = digits[:]
            for i in range(3):
                if not int(number[i]) in dig:
                    a = False
                else:
                    dig.remove(int(number[i]))
            if a:
                result.append(x)
    return result


digits = list(map(int, input("Enter a space-separated list of integers: ").split()))
print(EvenNumbers(digits))
