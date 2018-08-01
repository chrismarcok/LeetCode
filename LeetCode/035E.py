class Solution(object):
    def searchInsert(self, arr, num):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if num in arr:
            return arr.index(num)
        else:
            if num > max(arr):
                return len(arr)
            for x in range(len(arr)):
                if num < arr[x]:
                    return x
