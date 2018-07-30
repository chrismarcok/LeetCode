class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                res.append("FizzBuzz")
            elif x % 3 == 0:
                res.append("Fizz")
            elif x % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(x))
        return res