class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's
        curSum = 0
        maxSum = nums[0]

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum
        
        