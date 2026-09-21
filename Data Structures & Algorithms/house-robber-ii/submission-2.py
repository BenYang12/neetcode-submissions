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
        if not nums:
            return 0
    
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]





        