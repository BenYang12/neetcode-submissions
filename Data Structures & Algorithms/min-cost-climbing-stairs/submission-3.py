class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #cost[i] = cost of taking step from ith floor of a staircase
        #return min cost to reach top of staircase
        # 0 0 _ _ _ _ _ top

        #bottom up dp: let dp[i] represent min cost to reach step i
        #to reach each step i, I can come from step i - 1 or step i - 2

        n = len(cost) 
        #dp table
        dp = [0] * (n + 1)

        #base cases -> we can start at step 0 or 1 for free!
        dp[0] = 0
        dp[1] = 0

        #recurrence
        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        
        return dp[n]



        