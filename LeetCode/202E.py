class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        
        while (n is not 1):
            s = str(n)
            sum = 0
            
            for char in s:
                sum += int(char) ** 2
            if sum not in d:
                d[sum] = "seen"
            else:
                return False
            n = sum
        return True