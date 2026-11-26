class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # array nums (contains duplicates) -> return all possible subsets
        # solution must not contain duplicate subsets
        # can return solution in any order


        # Backtracking (DFS)
        # at every num...
        # include nums[i], exclude nums[i]

        # TC: O(2^n)
        # SC: O(h)

        res = []
        subset = []
        nums.sort()


        def dfs(i):
            if i >= len(nums):
                # reach end of array, current array represents a subset, store it
                res.append(subset.copy())
                return 
            

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()


            # exclude nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return res
                
        