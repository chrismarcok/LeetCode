import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1+nums2
        res.sort()
        return self.findMedian(res)
    def findMedian(self,nums):
        """
        >>> findMedian([1,3])
        2
        >>> findMedian([2])
        2
        """
        if len(nums) % 2 == 1:
            return nums[math.floor(len(nums) / 2)]
        else:
            return (nums[int(len(nums)/2)] + nums[int(len(nums)/2) - 1]) / 2