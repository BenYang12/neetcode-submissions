class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #given array distinct integers nums, target -> return all unique combos of nums where sum is target
        #same number may be chosen from nums unlimited number of times
        #two combinations are same if frequency of each of chosen numbers are teh same
        #one branch allowed to hold nums[i], other branch doesn't have it at all

        #TC: 2 decisions each time, height is at most target -> O(2^t)

        cur, combs = [], []

        def dfs(i,cur, combs, total):

            #base case
            if total == target:
                combs.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            
            #include nums[i]
            cur.append(nums[i])
            dfs(i, cur, combs, total + nums[i])


            #don't include nums[i]
            cur.pop()
            dfs(i + 1, cur,combs, total)
        dfs(0, cur, combs, 0)
        return combs
