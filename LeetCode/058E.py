class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        else:
            s = s.strip()
            return len(s.split(" ")[-1])
