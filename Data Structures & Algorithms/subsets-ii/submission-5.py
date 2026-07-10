class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #input is array of integers that may contain duplicates -> subsets
        nums.sort()

        curSet, subsets = [], []

        def dfs(i, curSet, subsets):

            #base case -> out of bounds 
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            

            #include nums[i]
            curSet.append(nums[i])
            dfs(i + 1, curSet, subsets)


            #don't include nums[i]
            #[1,2,2,3]
            curSet.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i + 1, curSet, subsets)
        dfs(0, curSet, subsets)
        return subsets

            



        