class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1, text2 -> return length of longest common subsequence
        # bottom-up DP
        #let dp[i][j] represent LCS of text1[:i], text2[:j]

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j+1], dp[i +1][j])
        
        return dp[m][n]



        



        
        