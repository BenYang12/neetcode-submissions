class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # 0 ..... 7
        dp[0] = 0


        #start computing every value in dp
        #go from 1 all the way to amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # 1 comes from current coin, dp[a - c] comes from complement that sums to amount
                    #coin = 4
                    #amount = 7
                    #dp[7] = 1 + dp[3]
        return dp[amount] if dp[amount] != float('inf') else -1

        