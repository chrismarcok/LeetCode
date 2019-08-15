class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        num = 0
        for char in s:
            num += ord(char)
            
        for char in t:
            num -= ord(char)
            
        return chr(-num)