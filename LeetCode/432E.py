class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s= (str(bin(num)))[2:]
        if (num < 0):
            return False
        
        if (s.count('1') == 1 and s.count('0') % 2 == 0):
            return True
        return False
        
        