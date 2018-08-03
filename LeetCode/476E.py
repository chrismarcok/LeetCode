class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        r = ""
        a = "{0:b}".format(num)
        for ch in a:
            if ch == "1":
                r += "0"
            else:
                r += "1"
        return int(r, 2)