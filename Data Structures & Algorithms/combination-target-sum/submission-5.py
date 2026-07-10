class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combs = []

        def dfs(i, curComb, total):

            #base case: total == target
            if total == target:
                combs.append(curComb.copy())
                return


            #base case: i out of bounds or sum too large (no point in further exploration)
            if i >= len(nums) or total > target:
                return 

            #include nums[i]
            curComb.append(nums[i])
            dfs(i, curComb, total + nums[i])


            curComb.pop()

            #cannot include nums[i] anywhere!
            dfs(i + 1, curComb, total)
        dfs(0, [], 0)
        return combs




        