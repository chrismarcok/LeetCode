class Solution:
    def twoSum(self, nums, target):
        """
        >>> twoSum([3,2,4], 6)
        [1, 2]
        """
        lst = []
        index1 = 0
        pairNum = 0

        for x in range(len(nums)):
            pairNum = target - nums[x]
            if pairNum in nums and (nums.count(pairNum) > 1 or pairNum != target//2):
                lst.append(x)
                index1 = x
                break
        for x in range(len(nums)):
            if x == index1:
                continue
            elif nums[x] == pairNum:

                lst.append(x)
                break
        return lst

