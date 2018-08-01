class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        a = 0

        for x in range(len(nums)):
            if nums[x] == 1:
                a += 1
            else:
                lst.append(a)
                a = 0
        lst.append(a)
        return max(lst)
