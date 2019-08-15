class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds = []
        evens = []
        for x in range(len(A)):
            if A[x] % 2 == 0:
                evens.append(A[x])
            else:
                odds.append(A[x])
        
        result = []
        for x in range(len(odds)):
            result.append(evens[x])
            result.append(odds[x])
        return result