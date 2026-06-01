class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #BRUTE FORCE
        res = 0 #area
        for L in range (len(heights)):
            for R in range(L+1, len(heights)):
                #compute area
                area = (R-L) * min(heights[R], heights[L])
                res = max(res,area) #update max

        return res


        