class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #find subarray with largest sum and return sum
        #kadane's alg

        res = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            res = max(res, curSum)

        return res

        