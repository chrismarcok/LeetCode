class Solution:
    def fib(self, N: int) -> int:
        d ={}
        return self.helper(d, N)
        
    def helper(self, d, n):
        if n == 0:
            return 0
        if (n == 2 or n ==1):
            return 1
        if (n in d):
            return d[n]
        else:
            d[n] = self.helper(d, n - 1) + self.helper(d, n - 2)
            return d[n]
        