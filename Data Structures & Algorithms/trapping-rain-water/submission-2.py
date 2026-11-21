class Solution:
    def trap(self, height: List[int]) -> int:

        # water at any position depends on shorter wall between left and right
        # if left wall is shorter, right wall can't help us
        # Thus, we can safely move the left pointer inward and calculate how much water can be trapped there
        # similarly, if the right wall is shorter, move the right pointer left


        # as we move pointers, keep track of highest wall seen so far on each side
        # leftMax and rightMax
        # water at each position is simply -> max wall on that side - height at that position

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                res += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                res += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])
            
        return res
           
                
                

                
        