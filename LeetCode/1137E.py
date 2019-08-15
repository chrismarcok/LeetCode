class Solution:
    def tribonacci(self, n: int) -> int:
        d={0: 0, 1: 1, 2: 1}
        return self.helper(d, n)
    
    def helper(self, d, n):
        if n in d:
            return d[n]
        else:
            d[n] = self.helper(d, n - 3) + self.helper(d, n - 2) + self.helper(d, n - 1)
            return d[n]