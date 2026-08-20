class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #given integer array nums -> find subarray that has largest product
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax 
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(tmp * num, curMin * num, num)
            res = max(res, curMax)
        return res

        


        