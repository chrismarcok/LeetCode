class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        p = {}
        
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        
        for char in t:
            if char not in p:
                p[char] = 0
            p[char] += 1
        
        return d == p