class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def helper(nums):
            #[rob1, rob2, n, n + 1]
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            rob1 = nums[0]
            rob2 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                tmp = rob2
                rob2 = max(nums[i] + rob1, rob2)
                rob1 = tmp
            return rob2

        #because houses are in a circle, you cannot rob both the first and last house
        #split problem into two linear cases:
        #1. exclude first house
        #2. exclude last house
        #each case becomes normal House Robber I problem
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))






        