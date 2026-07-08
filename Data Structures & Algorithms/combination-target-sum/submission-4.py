class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curComb, combs = [], []
        

        def dfs(i, curComb, combs, total):
            if total == target:
                combs.append(curComb.copy())
                return

            if i >= len(nums) or total > target:
                return

            
            #include nums[i]
            curComb.append(nums[i])
            dfs(i, curComb, combs, total + nums[i])
            curComb.pop()


            #don't include nums[i]
            dfs(i + 1, curComb, combs, total)

        dfs(0, curComb, combs, 0)
        return combs


        