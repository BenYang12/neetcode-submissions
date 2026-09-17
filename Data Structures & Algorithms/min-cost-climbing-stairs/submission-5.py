class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = [1, 2, 3]
        # 0 0 1 2
        # return 2
        # go left to right
        # last term should be 0
        # bottom up DP
        # let dp[i] represent minimum cost to reach step i
        # to reach step i...
        # 1. come from step i - 1 after spending dp[i - 1] + cost[i - 1]
        # 2. come from step i - 2 after spending dp[i - 2] + cost[i - 2]
        # base cases -> dp[0], dp[1] = 0, 0 since we can start at step 0 or 1 for free

        n = len(cost)
        dp = [0] * (n + 1)

        #base case
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i-2])

        return dp[n]



