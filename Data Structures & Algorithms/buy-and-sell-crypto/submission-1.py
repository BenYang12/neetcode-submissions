class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #sliding window
        L = 0
        maxP = 0

        for R in range(len(prices)):
            if prices[L] > prices[R]:
                L = R
            profit = prices[R] - prices[L]
            maxP = max(maxP, profit)
        return maxP

        
        
        
        
        