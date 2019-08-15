class Solution {
    public int minPathSum(int[][] grid){ 
        int[][] distances = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                distances[i][j] = -1;
            }
        }
        return getMin(distances, grid, 0, 0);
    }
    
    public int getMin(int[][] distances, int[][] grid, int m, int n){
        if (distances[m][n] != -1){
            return distances[m][n];
        }
        else if (m == grid.length - 1 && n == grid[0].length - 1) {
            distances[m][n] = grid[m][n];
            return distances[m][n];
        }
        else if (m == grid.length - 1){
            distances[m][n] = grid[m][n] + getMin(distances, grid, m, n + 1);
            return distances[m][n];
        } else if (n == grid[0].length - 1){
            distances[m][n] = grid[m][n] + getMin(distances, grid, m + 1, n);
            return distances[m][n];
        }
        else {
            distances[m][n] = Math.min(
                getMin(distances, grid, m + 1, n),
                getMin(distances, grid, m, n + 1)
            ) + grid[m][n];
            return distances[m][n];
        }
    }
}