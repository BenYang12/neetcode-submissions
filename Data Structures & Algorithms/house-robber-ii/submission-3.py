class Solution:
    def rob(self, nums: List[int]) -> int:
        # essentially House Robber I, but houses are arranged in a circle 
        # first and last house are neighbors
        # split problem into two linear cases
        # rob houses from index 1 to n - 1, then from index 0 to n - 2
        # each case becomes normal House Robber 1 problem
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    # house robber 1 helper function
    def helper(self, nums):
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
            dp[i] = max(nums[i] + dp[i - 2],dp[i - 1])

        return dp[-1]




        