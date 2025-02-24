# 24/02/2025
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s):
    ascii_characters = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    if 1 <= len(s) <= 5 * 104:
        for i in range(len(s)):
            if not i in ascii_characters:
                return s
            if s[i] == " ":
                try:
                    if s[i+1] == " ":
                        return s
                except:
                    pass
        word = ""
        final_result = ""
        for i in s:
            if i == " ":
                final_result = final_result + word + i
                word = ""
            else:
                word = i + word
        final_result += word
        return final_result


string = input("Enter a string: ")
print(reverseWords(string))

