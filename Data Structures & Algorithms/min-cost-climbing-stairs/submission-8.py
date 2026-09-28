class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] = cost of taking step from ith floor of staircase 
        # pay cost -> take 1 or 2 steps
        # choose to start at index 0 or index 1
        # return min cost to reach top of staircase

        #1-D DP -> let dp[i] represent cost to reach ith step
        # cost = [1,2,3] goal
        # dp = 0 0 _ _ 
        # we can come from i - 1 or i - 2
        # return last element in dp

        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]

        