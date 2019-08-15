class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lst = []
        sumNum = 0
        first = True
        for query in queries:
            temp = A[query[1]]
            A[query[1]] += query[0]
            if first:
                sumNum = sum([A[x] for x in range(len(A)) if A[x] % 2 == 0])
            else:
                if query[0] % 2 == 0:
                    if (A[query[1]] % 2  == 0):
                        sumNum += query[0]
                    else:
                        sumNum += 0
                else: # we added an odd number
                    if (A[query[1]] % 2  == 0):
                        sumNum += A[query[1]]
                    else:
                        sumNum -= temp
                        
            lst.append(sumNum)
            first = False
        return lst
    