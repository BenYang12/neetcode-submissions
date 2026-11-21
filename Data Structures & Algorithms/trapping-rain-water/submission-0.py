class Solution:
    def trap(self, height: List[int]) -> int:
        # amoutn of water that can be trapped: min(L, R) - h[i] >= 0
        # negative = trap zero water

        # O(n) time, O(n) space
        # maxLeft, maxRight, and min(L,R) arrays


    
        # TWO POINTTER -> O(n) time, O(1) space
        # maxL, maxR -> max on left and right so far
        # shift the one that has smaller max value
        # use maxL and maxR to calculate min(L, R) - h[i] >= 0


        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res





      


  

    





        