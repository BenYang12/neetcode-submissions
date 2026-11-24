class Solution:
    def trap(self, height: list[int]) -> int:
        # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # Output: 6

        n = len(height)
        if n == 0:
            return 0


        # TC: O(n)
        # SC: O(n)
        leftMax = [0] * n # tallest bar from start up to index i
        rightMax = [0] * n # tallest bar from end up to index i
        # trapped water at position i = min(leftMax[i], rightMax[i]) - height[i]


        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        

        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        

        return res

        
        


        



       