class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        d = {}
        for x in range(length):
            if A[x] not in d:
                d[A[x]] = 1
            else:
                return A[x]