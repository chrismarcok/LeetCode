class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == [] or k == 0 or len(nums) == 1:
            return
        k %= len(nums)
        for x in range(k):
            last = nums[-1]
            del nums[-1]
            nums.insert(0, last)
