class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, curComb, total,  nums, target):

            #base case
            if total == target:
                res.append(curComb.copy())
                return
            
            if i >= len(nums) or total > target:
                return 
            

            #include
            curComb.append(nums[i])
            helper(i, curComb, total + nums[i], nums, target)

            #don't include
            curComb.pop()
            helper(i + 1, curComb, total, nums, target)

        helper(0,[],0, nums,target)
        return res
        