class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for x in range(0, len(nums), 2):
            sum += nums[x]
        return sum
