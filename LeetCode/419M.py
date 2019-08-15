class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        finished = False
        
        while not finished:
            finished = True
            for m in range(len(board)):
                for n in range(len(board[0])):
                    finished = True
                    if board[m][n] == 'X' and self.hasNeighbours(board, m, n):
                        board[m][n] = "."
                        finished = False
                        
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == "X":
                    count += 1
                        
        return count
    
    def hasNeighbours(self, board, m, n):
        try:
            if board[m + 1][n] == "X":
                return True
        except:
            print("")
        try:
            if board[m][n + 1] == "X":
                return True   
        except:
            print("")
        
        return False