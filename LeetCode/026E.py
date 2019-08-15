class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        x= 0
        while (x < len(nums)):
            if nums[x] not in d:
                d[nums[x]] = "xd"
                x += 1
            else:
                del nums[x]
                continue
            
        return len(nums)