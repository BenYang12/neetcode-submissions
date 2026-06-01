class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer solution, start with L at start and R at end
        #shrink the "window", if I decrease the width, I want to increase the height -> keep the pointer with higher height
        #calculate area for "window"
        L = 0
        R = len(heights) - 1
        maxArea = 0

        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            maxArea = max(area, maxArea)

            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
                
        return maxArea


        