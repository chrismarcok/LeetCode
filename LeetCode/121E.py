class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        diff = 0
        low = prices[0]
        high = prices[0]
        
        for x in range(len(prices)):
            if prices[x] < low:
                high = 0
                low = prices[x]
            elif prices[x] > high:
                high = prices[x]
                            
            if high - low > diff:
                diff = high - low
                
        return diff