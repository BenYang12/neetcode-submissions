class Solution:
    def trap(self, height: List[int]) -> int:
        # Prefix and Suffix Arrays
        # O(n) time, O(n) space


        # precompute tallest bar to left and right for every index
        # leftMax[i] = tallest bar from start up to index i
        # rightMax[i] = tallest bar from end up to index i

        # water trapped at position i = min(leftMax[i], rightMax[i]) - height[i]
        

        n = len(height)
        if n == 0:
            return 0
        

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        
        rightMax[n - 1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]

        return res
        