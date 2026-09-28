class Solution:
    def climbStairs(self, n: int) -> int:

        # n = number of steps to reach top of staircase
        # return number of distinct ways to climb to top


        # n = 3
        # top 1 2 _
        # 2 1 top

        #edge cases
        if n <= 2:
            return n
        
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        

        return dp[-1]

        