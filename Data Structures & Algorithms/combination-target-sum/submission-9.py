class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array of distinct ints, integer target -> return all unique combos that sum to target
        # same number may be chosen from nums unlimited number of times

        # Optimized
        # avoid exploring useless paths by using sorting + early stopping
        # sort nums so once num makes the sum exceed target, all numbers after it
        # will also exceed target -> safely stop exploring further

        # at each position, try every number starting from index i, allowing reuse 
        # build combinations step-by-step
        # whenever running total equals target, record current list

        res = []
        nums.sort()

        def dfs(i, comb, total):
            # base cases
            if total == target:
                res.append(comb.copy())
                return 

            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                comb.append(nums[j])
                dfs(j, comb, total + nums[j])
                comb.pop()
                
            
           
        
        dfs(0, [], 0)
        return res


            


       

        
        