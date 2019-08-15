class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int[][] numWays = new int[grid.length][grid[0].length];
        
        //init all zeros
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                numWays[i][j] = 0;
            }
        }
        numWays[0][0] = 1;
        
        
        for (int i = 0; i < grid.length; i++){
            //go down the row. (advancing col.)
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){ //IS an obstacle
                    numWays[i][j] = 0;
                } else if (i == 0 && j ==0){
                    continue;
                }
                else if (i == 0){ //first row
                    numWays[i][j] = numWays[i][j - 1];
                } else if (j == 0){ // first col
                    numWays[i][j] = numWays[i - 1][j];
                } else {
                    numWays[i][j] = numWays[i - 1][j] + numWays[i][j - 1];    
                }
                
            }
        }
        
        return numWays[grid.length - 1][grid[0].length - 1];
    }
}