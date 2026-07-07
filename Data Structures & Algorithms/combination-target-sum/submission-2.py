class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #array of distinct integers nums and target integer -> return unique combinations of nums where chosen numbers sum to target
        #same number may be chosen from nums an unlimited number of times
        #two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise, they are different

        combs = []
        total = 0

    
        def helper(i,curComb, total, nums, target, combs):

            if total == target:
                combs.append(curComb.copy())
                return

            if i >= len(nums) or total >= target:
                return
            


            #include
            curComb.append(nums[i])
            helper(i, curComb, total + nums[i], nums, target, combs)
            curComb.pop()

            #don't include
            helper(i + 1, curComb, total, nums, target, combs)
        
        helper(0,[], total, nums, target, combs)
        return combs




        