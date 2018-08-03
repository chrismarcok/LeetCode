class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = "{0:b}".format(n)
        last = n[0]
        for ch in range(1, len(n)):
            if n[ch] == last:
                return False
            else:
                last = n[ch]
        return True
                