class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up dp
        # let dp[r][c] = number of unique ways from (r,c) to end
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for r in range(m -1, -1, -1):
            for c in range(n -1, -1, -1):
                dp[r][c] += dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
         