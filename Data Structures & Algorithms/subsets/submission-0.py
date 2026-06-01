class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            #base case -> if i is out of bounds
            if i >= len(nums):
                res.append(subset.copy()) #subset is gonnna be modified
                return

        
            #left decision, include
            subset.append(nums[i])
            dfs(i+1) #recursively run dfs on next element


            #right decision, don't include
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res







        