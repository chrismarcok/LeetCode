class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("D") == moves.count("U") and moves.count("L") == moves.count("R")
