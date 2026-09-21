class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums = [1,1,3,3]
        # output = 4

        # dp[i] = max money up to house i
        # 1 1 _ _ 


        # edge cases
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n 

        

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)


        