class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights[i] represents height of ith bar

        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)


            if heights[l] >= heights[r]:
                r -= 1

            else:
                l += 1
                
        return res
        


        