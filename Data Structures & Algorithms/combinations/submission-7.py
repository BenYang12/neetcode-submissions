class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Backtracking: Trivial
        # binary choice: include/exclude
        # TC: O(k * 2^n), SC: O(n)

        res = []
        def dfs(i, comb):
            # base case
            if len(comb) == k:
                res.append(comb.copy())
                return 

            if i > n:
                return
            
            
            

            # include
            comb.append(i)
            dfs(i + 1, comb)
            comb.pop()

            # exclude
            dfs(i + 1, comb)
        
        dfs(1, [])
        return res
        



        