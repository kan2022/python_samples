# 07/08/26
# Link: https://leetcode.com/problems/odd-string-difference/

class Solution:
    def oddString(self, words: List[str]) -> str:
        results = []
        for i in words:
            track = []
            for j in range(len(i) - 1):
                track.append(ord(i[j + 1]) - ord(i[j]))
            results.append(track)
        n = 0
        m = 0
        for i in range(len(results)):
            inp = results[i]
            if i == 0:
                n = inp
            elif i == 1:
                m = inp
                count = 0
            elif n != m:
                if m == inp:
                    return words[0]
                return words[1]
            else:
                if count == 0:
                    if inp == n == m or inp == n:
                        a = n
                    else:
                        a = m
                    count += 1
                if a != inp:
                    return words[i]
