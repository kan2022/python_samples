# 23/02/2025
# Link: https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):
    if not 1 <= len(s) <= 1000:
        return s
    aList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    test_s = s.lower()
    for i in test_s:
        if i not in aList:
            return s

    def solutionA(s):
        final_result = []
        result = ""
        for i in range(1, len(s)-1):
            if s[i-1] == s[i+1]:
                result = s[i-1] + s[i] + s[i+1]
                counter = 4
                if i+2 == len(s):
                    final_result.append(result)
                    break
                if i-2 < 0:
                    final_result.append(result)
                    continue
                for j in range(i+2, len(s)+1):
                    if j - counter < 0 or s[j] != s[j-counter]:
                        final_result.append(result)
                        break
                    result += s[j]
                    result = s[j-counter] + result
                    counter += 2
                final_result.append(result)

        if len(final_result) == 0:
            return result
        solution = ""
        for i in range(len(final_result)):
            if len(final_result[i]) > len(solution):
                solution = final_result[i]
        return solution
    
    def solutionB(s):
        final_result = []
        result = ""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                result = s[i] + s[i+1]
                if i+2 == len(s):
                    final_result.append(result)
                    break
                for j in range(i+2, len(s)):
                    if result[0] == s[j]:
                        result += s[j]
                        if j == len(s)-1:
                            final_result.append(result)
                    else:
                        final_result.append(result)
                        break

        if len(final_result) == 0:
            return result
        solution = ""
        for i in range(len(final_result)):
            if len(final_result[i]) > len(solution):
                solution = final_result[i]
        return solution
    
    def solutionC(s):
        final_result = []
        result = ""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                result = s[i] + s[i+1]
                if i+2 == len(s):
                    final_result.append(result)
                    break
                counter = 3
                if i+2 - counter < 0:
                    final_result.append(result)
                    continue
                for j in range(i+2, len(s)):
                    if j - counter < 0 or s[j] != s[j-counter]:
                        final_result.append(result)
                        break
                    result += s[j]
                    result = s[j-counter] + result
                    counter += 2
                final_result.append(result)
        
        if len(final_result) == 0:
            return result
        solution = ""
        for i in range(len(final_result)):
            if len(final_result[i]) > len(solution):
                solution = final_result[i]
        return solution

    final = {len(solutionA(s)): solutionA(s),
            len(solutionB(s)): solutionB(s),
            len(solutionC(s)): solutionC(s)}
    len_answer = 0
    answer = solutionA(s)
    for i in final.keys():
        if len_answer < i:
            len_answer = i
            answer = final[i]
    if len(answer) == 0:
        return s[0]
    return answer


string = input("Enter a string: ")
print(longestPalindrome(string))

