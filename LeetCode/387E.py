class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        for x in range(len(s)):
            if d[s[x]] == 1:
                return x
        return -1