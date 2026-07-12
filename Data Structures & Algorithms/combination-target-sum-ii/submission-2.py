class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #candidates array w/ duplicates, target -> return all unique combinations that sum to target
        #each element from candidates may be chosen at most once within a combination

        candidates.sort() #sort in ascending order to group duplicates adjacently
        cur, combs = [], []


        def dfs(i, total):

            #base case
            if total == target:
                combs.append(cur.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            
            #include
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])


            #don't include 
            cur.pop() #cleanup
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total )
        dfs(0,0)
        return combs



    
        