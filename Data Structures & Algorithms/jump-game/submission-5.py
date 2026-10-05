class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # input is nums, where nums[i] indicates maximum jump length at that position
        # return true if I can reach last index starting from 0

        # nums = [1,2, 0, 1, 0]

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
    



