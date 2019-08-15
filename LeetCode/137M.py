class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        
        for x in nums:
            if x not in d:
                d[x] = 0
            d[x] += 1
        for x in d:
            if d[x] == 1:
                return x