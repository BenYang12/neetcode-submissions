class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,0,1,0]
        # nums -> nums[i] indicates max jump length at position
        # return true if I can reach last index starting from 0

        #greedy approach -> set target at end
        #iterate from end towards beginning
        #start from second to last index
        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        
        return True if target == 0 else False


        