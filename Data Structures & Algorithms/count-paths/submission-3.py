class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # optimize with bottom-up DP
        # TC: O(m * n), SC: O(m * n)


        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case, only one way to stay at destination
        dp[m - 1][n - 1] = 1

        # recurrence -> for any cell, number of unique paths to the destination is 
        # paths from the cell below + paths from teh cell to the right
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] += dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]
        