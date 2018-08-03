class Solution:
    def addDigits(self, n):
        """
        :type num: int
        :rtype: int
        """
        if n < 10:
            return n
        else:
            sum = 0
            while n > 0:
                sum += n % 10
                n = n // 10
            if sum < 10:
                return sum
            else:
                return self.addDigits(sum)
