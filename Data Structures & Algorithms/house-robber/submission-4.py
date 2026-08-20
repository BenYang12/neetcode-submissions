class Solution:
    def rob(self, nums: List[int]) -> int:
        #integer array nums, return max amount of money I can rob
        #nums = [1, 1, 4, 4]

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]



        rob1 = nums[0]
        rob2 = max(nums[0], nums[1]) #base case

        for i in range(2,len(nums)):
            tmp = rob2
            rob2 = max(nums[i] + rob1, rob2)
            #shift rob1 
            rob1 = tmp
        return rob2


    
    
       