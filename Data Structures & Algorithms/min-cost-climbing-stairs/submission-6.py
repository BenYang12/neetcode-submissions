class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = [1, 2, 3]
        # res = 2


        # dp[i] = cost needed to get to index i
        # 0 0 1 2

        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]




        