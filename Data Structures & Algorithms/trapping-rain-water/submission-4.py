class Solution:
    def trap(self, height: list[int]) -> int:
        # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # Output: 6

        n = len(height)
        if n == 0:
            return 0
        
        # water at any point depends on the shorter wall between the left and right sides
        # left wall shorter -> right wall can't help us (water limited by left side)
        # thus, we can safely move left pointer inward and calculate how much water can be trapped there

        # TC: O(n)
        # SC: O(1)
        

        l = 0
        r = n - 1
        maxL = height[l]
        maxR = height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                res += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                # maxR < maxL
                res += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
        return res





       

        
        


        



       