class Solution:
    def climbStairs(self, n: int) -> int:
        # to reach step i, can only come from step i - 1 and i - 2
        # total ways to reach step i is sum of ways to reach the previous two steps
        

        # n = 3
        # top 1 2 3 

        if n <= 2:
            return n

        #bottom-up dp
        #dp array where dp[i] = number of ways to reach step i
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
       
         