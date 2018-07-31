class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for row in range((len(grid))):
            for element in range(len(grid[row])):
                if grid[row][element] == 0:
                    continue
                topNeighbors = True
                leftNeighbors = True
                rightNeighbors = True
                botNeighbors = True
                if (row == 0):
                    topNeighbors = False
                if element == 0:
                    leftNeighbors = False
                if element == len(grid[0]) - 1: # if the element is equal to the number of columns
                    rightNeighbors = False
                if row == len(grid) - 1: # if the element is equal to the number of rows
                    botNeighbors = False

                numNeighbors = 4

                if topNeighbors and grid[row - 1][element] == 1:
                    numNeighbors -= 1
                if leftNeighbors and grid[row][element - 1] == 1:
                    numNeighbors -= 1
                if rightNeighbors and grid[row][element + 1] == 1:
                    numNeighbors -= 1
                if botNeighbors and grid[row + 1][element] == 1:
                    numNeighbors -= 1
                perimeter += numNeighbors
        return perimeter
