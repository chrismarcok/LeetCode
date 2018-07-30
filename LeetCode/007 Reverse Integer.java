class Solution {
    public int reverse(int x) {
        boolean neg = false;
        if (x < 0)
            neg = true;
        String str = String.valueOf(x);
        if (neg)
            str = str.substring(1);
        String result = "";
        for(int i = str.length() - 1; i >= 0; i--){
            result += "" + str.charAt(i);
        }
        
        while (result.charAt(0) == '0' && result.length() != 1){
            result = result.substring(1);
        }
        
        
        if (neg)
            result = "-" + result;
        
        int y;
        
        try{
            y = Integer.parseInt(result);
        } catch (NumberFormatException e){
            y = 0;
        }
        
        return y;
    }
}