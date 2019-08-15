class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLst = []
        colLst = []
        
        
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    rowLst.append(m)
                    colLst.append(n)
                
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if (m in rowLst or n in colLst):
                    matrix[m][n] = 0
                        
                    
                    
        
        