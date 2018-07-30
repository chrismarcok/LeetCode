class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        
        for x in range(len(S)):
            if S[x] in J:
                num += 1
        return num