class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Backtracking, DFS
        subSets = []
        curSet = []


        def dfs(i,nums,curSet,subSets):
            if i >= len(nums):
                subSets.append(curSet.copy())
                return

            
            #include i
            curSet.append(nums[i])
            dfs(i + 1, nums, curSet, subSets)


            #don't include i
            curSet.pop()
            dfs(i+1, nums, curSet, subSets)

        dfs(0, nums, curSet, subSets)
        return subSets
            


        