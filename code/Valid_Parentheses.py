# 10/10/2024
# Link: https://leetcode.com/problems/valid-parentheses/

def check_parentheses(s):
    matching_bracket = {')': '(', '}': '{', ']': '['}
    stack = []
    stack_size = 0

    for h in s:
        if h in matching_bracket.values():
            stack.append(h)
            stack_size += 1
        elif h in matching_bracket.keys():
            if stack_size == 0 or matching_bracket[h] != stack[stack_size - 1]:
                return False
            stack = stack[:-1]
            stack_size -= 1
        else:
            return False

    return stack_size == 0


print("Input a string of parentheses and I will tell you if it is valid:")
parentheses = input()
print(check_parentheses(parentheses))

