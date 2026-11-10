class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights -> choose any two bars (heights) to form a container
        # return max amount of water 


        # TWO POINTER
        # l -> beginning, r -> end 
        # TC: O(n)
        # SC: O(1)
        
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1


            res = max(area, res)
            
        
        return res




        