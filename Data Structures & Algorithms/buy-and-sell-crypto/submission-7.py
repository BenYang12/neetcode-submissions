class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price of NeetCoin on ith day

        # sliding window
        # profit is when prices[r] > prices[l]
        # sweep across prices with r, prices[r] < prices[r] -> loss -> shift l to r
        # TC: O(n)
        # SC: O(1)
        res = 0
        l = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            
            profit = prices[r] - prices[l]
            res = max(res, profit)
        
        return res
        