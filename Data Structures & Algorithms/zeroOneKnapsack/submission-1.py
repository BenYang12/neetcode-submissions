class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        # Solve 0/1 Knapsack problem
        # calculate max profit I can achieve w/o exceeding capacity
        # bottom up DP -> tabulation


        #DP table, capacity = cols, items = rows
        N = len(profit)
        M = capacity
        dp = [[0] *(M + 1) for _ in range(N)]

        #first col -> all zeros
        for i in range(N):
            dp[i][0] = 0
        
        #first row -> some zeros, some profit[0]
        for c in range(M + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]

        #recurrence
        for r in range(1, N):
            for c in range(1, M + 1):
                skip = dp[r - 1][c]
                include = 0

                if weight[r] <= c:
                    include = profit[r] + dp[r - 1][c - weight[r]]

                dp[r][c] = max(skip, include)
        return dp[N - 1][M]
        




