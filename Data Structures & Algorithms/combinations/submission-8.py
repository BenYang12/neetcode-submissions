class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Backtracking: Optimal
        # instead of making include/exclude decisions, iterate through available
        # numbers and always include one. 

        # starting from given position ensures we never revisit smaller numbers
        # avoiding duplicates. Stop when the combination reaches size k

        res = []

        def dfs(i,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(i, n + 1):
                comb.append(i)
                dfs(i + 1, comb)
                comb.pop()
            

        dfs(1, [])
        return res

            
        