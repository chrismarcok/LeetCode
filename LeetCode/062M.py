import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n = n, m
        return self.nCr(m + n - 2, m - 1)

    def nCr(self, n, r):
        f = math.factorial
        return f(n) // f(r) // f(n - r)
