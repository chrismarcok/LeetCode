class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif len(needle) > len(haystack):
            return -1
        for x in range(len(haystack) - len(needle) + 1):
            if haystack[x:x + len(needle)] == needle:
                return x
        return -1
