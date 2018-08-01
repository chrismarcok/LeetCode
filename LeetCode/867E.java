class Solution {
    public int[][] transpose(int[][] A) {
        int[][] tranny = new int[A[0].length][A.length];
        for (int i = 0; i < A[0].length; i++)  {
            for (int j = 0; j < A.length; j++)
                tranny[i][j] = A[j][i];
        }
      return tranny;
    }
}