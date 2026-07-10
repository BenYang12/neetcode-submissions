class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #input is array of unique integers -> return all possible subsets
        subset, subsets = [], []

        def dfs(i, subset, subsets):

            #base case
            if i >= len(nums):
                subsets.append(subset.copy())
                return

            
            #include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset, subsets)

            subset.pop()
            dfs(i + 1, subset, subsets)
        
        dfs(0, subset, subsets)
        return subsets
        
        