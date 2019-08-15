class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        d = {}
        
        for x in range(len(nums)):
            if nums[x] not in d:
                d[nums[x]] = 0
            d[nums[x]] += 1
            
        for key in d:
            if d[key] == 1:
                lst.append(key)

        return lst