class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # return min cost to reach top of stair case 
        # bottom up DP with base cases
        # [1, 2, 3] 0

        # DP Table 
        # 0 is the target, so when we sum cost[i] with the step where we       increment by 2, it stays the same
        # _ _ 3 0 

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        return min(cost[0], cost[1])



        