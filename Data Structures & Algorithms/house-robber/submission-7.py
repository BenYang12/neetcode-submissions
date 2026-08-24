class Solution:
    def rob(self, nums: List[int]) -> int:
        # integer array nums -> nums[i] represents amount of money the ith house has
        # return maximum amount of money I can rob w/o alerting police


        # nums = [1, 1, 3, 3]

        # base cases -> first elem, then max of first two elem
        # dp = [1, 1, 4, 4 ]


        #edge cases
        if not nums:
            return 0
        
        if len(nums) < 2:
            return nums[0]
        


        rob1, rob2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = rob2
            rob2 = max(nums[i] + rob1, rob2)
            rob1 = tmp
        
        return rob2


            
        