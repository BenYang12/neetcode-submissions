class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums[] -> max product subarray        
        # kadane's + trick -> keep track of min product and max product
        # [-3, 0, -2] 
        # edge case -> 0 value will kill our streak
        # any time I see a 0, reset max and min to 1

        #can't just set res to start as 0
        #[-1] -> max product is -1, that is less than 0
        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            #when calculating curMin and curMax, handle 0s by including num
            tmp = curMin
            curMin = min(num * curMin, num * curMax, num )
            curMax = max(num * curMax, num * tmp, num)
            res = max(res, curMax)
        return res




