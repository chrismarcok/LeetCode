class Solution {
    public int[] diStringMatch(String S) {
        int largest = S.length();
        int smallest = 0;
        int[] ans = new int[S.length() + 1];
        
        for (int i = 0; i < S.length(); i++){
            if (S.charAt(i) == 'D'){
                ans[i] = largest;
                largest--;
            }
            else {
                ans[i] = smallest;
                smallest++;
            }
        }
        ans[ans.length - 1] = smallest;
        return ans;
    }
}