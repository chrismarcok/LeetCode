class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split(" ")
        r = ""
        for x in range(len(lst)):
            lst[x] = lst[x][::-1]
        for x in range(len(lst)):
            r += lst[x] + " "
        return r.strip(" ")
