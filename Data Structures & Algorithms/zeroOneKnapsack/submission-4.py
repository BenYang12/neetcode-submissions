class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        N = len(profit)
        M = capacity

        #create DP table
        dp = [[0] * (M + 1) for _ in range(N) ]

        #base case first row
        for c in range(M + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
       
        #base case first column
        for r in range(N):
            dp[r][0] = 0


        #recurrence
        for r in range(1, N):
            for c in range(1, M + 1):
                #skip this item -> go up
                skip = dp[r - 1][c]
                
                #include this item -> check, potentially go diagonal
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + dp[r - 1][c - weight[r]]

                dp[r][c] = max(skip, include)
        
        #return bottom right
        return dp[N - 1][M]

    
