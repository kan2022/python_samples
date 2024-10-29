# 05/10/2024
# Link: https://leetcode.com/problems/roman-to-integer/

def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    previous_value = 0
    total = 0

    for char in reversed(s):
        value = roman_values[char]
        if value < previous_value:
            total -= value
        else:
            total += value
        previous_value = value

    return total

print("Input a number in Roman numerals:")
s = input()
print(roman_to_int(s))

