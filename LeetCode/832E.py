class Solution:
    def flipAndInvertImage(self, Arr):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = Arr[:]
        for x in A:
            x.reverse()
            for y in range(len(x)):
                x[y] = abs(1-x[y])
        return A