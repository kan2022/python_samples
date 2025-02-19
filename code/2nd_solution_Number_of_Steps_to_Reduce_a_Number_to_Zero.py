# 19/02/25
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def reduce_steps(n):
    if not 0 <= n <= 10**6:
        return n
    result = 0
    while n > 0:
        result += 1
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            
    return result


num = int(input("Enter a number: "))
print(reduce_steps(num))

