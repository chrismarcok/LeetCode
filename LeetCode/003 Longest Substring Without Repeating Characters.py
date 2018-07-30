class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is "":
            return 0
        i , j = 0 ,0
        biggest = 0
        n = len(s)
        while(i < n and j < n):
            substr = s[i:j+1]
            if self.hasNoDuplicates(substr):
                biggest += 1
                j += 1
            else:
                i += 1
                j = i + biggest
        return biggest
        
    def hasNoDuplicates(self, s):
        return len(set(s)) == len(s)