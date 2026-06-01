class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window
        L = 0
        maxProfit = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)
        return maxProfit
        

            



        