class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #given array nums of unique integers -> return all subsets of nums
        #cannot contain any duplicate subsets

        subSets, curSet = [], []
        i = 0



        def dfs(i,nums, subSets, curSet):
            #base case
            if i >= len(nums):
                subSets.append(curSet.copy())
                return

            #include nums[i]
            curSet.append(nums[i])
            dfs(i + 1, nums, subSets, curSet)

            curSet.pop()


            #don't include nums[i]
            dfs(i+1, nums,subSets,curSet)
        
        dfs(i,nums,subSets,curSet)
        return subSets



        