class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        x, y = 0, 0
        for m in range(8):
            for n in range(8):
                if board[m][n] == "R":
                    x, y = m, n
        
        #north
        for i in range(x, -1, -1):
            if (board[i][y] == "B"):
                break
            elif (board[i][y] == "p"):
                count += 1
                break
        #east
        for i in range(y, 8):
            if (board[x][i] == "B"):
                break
            elif (board[x][i] == "p"):
                count += 1
                break
        #south
        for i in range(x, 8):
            if (board[i][y] == "B"):
                break
            elif (board[i][y] == "p"):
                count += 1
                break
        #west
        for i in range(y, -1, -1):
            if (board[x][i] == "B"):
                break
            elif (board[x][i] == "p"):
                count += 1
                break
        
        return count