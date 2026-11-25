class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums (unique elements) -> return all possible subsets
        # solution set must not contain duplicate subsets
        # in subsets, order doesn't matter


        # idea: build all possible subsets by making choice at each step:
        # for every number, include it or exclude it -> decision tree!
        # Backtracking (dfs): add the current number, explore further...
        # or remove it (undo), explore without it


        # Whenever we reach the end of the array, current list represents one
        # complete subset, so we store it


        # TC: O(n * 2^n)
        # SC: O(n)

        res = []
        subset = []

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # include
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()


            # don't include
            dfs(i + 1)
        
        dfs(0)
        return res
        



        