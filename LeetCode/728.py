class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lst = []
        for x in range(left, right + 1):
            if self.allNumsDiv(x):
                lst.append(x)
        return lst

    def allNumsDiv(self, x):
        num = x
        s = str(x)
        if s.count('0') > 0:
            return False

        while x >= 1:
            if num % (x % 10) == 0:
                x = x // 10
                continue
            else:
                return False
        return True
