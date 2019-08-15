class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x= 0
        while (x < len(nums)):
            if nums[x] == val:
                del nums[x]
                continue
            x += 1
        return len(nums)