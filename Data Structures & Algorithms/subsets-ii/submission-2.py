class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        #nums array may contain duplicates -> return all possible subsets
        #solution cannot contain duplicate subsets


        nums.sort() #sort nums to avoid duplicates
        curSet, subSets = [], []
        i = 0

        def dfs(i, nums, curSet, subSets):

            #base case
            if i >= len(nums):
                subSets.append(curSet.copy())
                return 
            
            #decision to include nums[i]
            curSet.append(nums[i])
            dfs(i + 1, nums, curSet, subSets)

            curSet.pop() #undo, remove nums[i]
            while i + 1 <= len(nums)-1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, nums, curSet, subSets)

            #one path includes 1 or more 2s, the other doesn't include any
        
        dfs(i,nums,curSet,subSets)
        return subSets

            





        