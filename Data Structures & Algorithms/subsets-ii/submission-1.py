class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #array num of integers, which may contain duplicates, return all possible subsets
        #sort elements first -> skip previous
        res = []
        curSet = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(curSet.copy())
                return

            
            #choice 1 -> include
            curSet.append(nums[i])
            backtrack(i + 1)

            #choice 2 -> don't include
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res



        