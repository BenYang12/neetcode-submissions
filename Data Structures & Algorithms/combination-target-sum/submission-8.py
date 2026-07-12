class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #input array of distinct integers, and int target -> return all unique combos that sum to target
        #same number may be chosen unlimited number of times, combo order does not matter


        cur, combs = [], []
       

        def dfs(i, total):

            #base case
            if total == target:
                combs.append(cur.copy())
                return

            #base case
            if i >= len(nums) or total > target:
                return
            

            #include nums[i]
            cur.append(nums[i])
            dfs(i, total + nums[i])

            #don't include nums[i]
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return combs
        