class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] is money ith house has
        # cannot rob two adjacent houses, return max amount of money

        # 1-D DP: let dp[i] represent max money up to house i
        # nums = [1, 1, 3, 3]
        # dp = 1 1 _ _


        # edge cases 

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2],dp[i - 1] )

        return dp[-1]



        