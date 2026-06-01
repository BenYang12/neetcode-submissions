class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        L = 0
        R = len(heights)-1

        while L < R:
            area = (R-L) * min(heights[R], heights[L])
            res = max(res,area)

            #update pointers based on height of each pointer

            if heights[L] < heights[R]:
                L +=1
            elif heights[R] < heights[L]:
                R -=1
            else:
                L+=1
        return res
            






        