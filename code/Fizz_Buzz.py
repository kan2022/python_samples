# 19/02/25
# Link: https://leetcode.com/problems/fizz-buzz/


def FizzBuzz(n):
    if not 1 <= n <= 10**4:
        return n
    result = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                result.append("FizzBuzz")
                continue
            result.append("Fizz")
            continue
        if i % 5 == 0:
            result.append("Buzz")
            continue
        result.append(str(i))
    return result


num = int(input("Enter a number between 1 and 10000 included: "))
print(FizzBuzz(num))

