class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = [1] * len(nums)
        R = [1] * len(nums)
        
        for x in range(1, len(nums)):
            L[x] = L[x-1] * nums[x-1]
        for x in range(len(nums) - 2, -1, -1):
            R[x] = R[x+1] * nums[x+1]
        return [R[x] * L[x] for x in range(len(nums))]