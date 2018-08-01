class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in range(len(nums)):
            s = str(nums[x])
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        for key in d:
            if d[key] == 1:
                return int(key)