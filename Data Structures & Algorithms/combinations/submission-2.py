class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #two integers n and k, return all possible combinations of k numbers chosen from the range [1,n]
        #backtracking -> recursive dfs
        res = []
        comb = []

        def backtrack(i):
            if len(comb) == k:
                res.append(comb.copy())
                return 
            if i > n:
                return 

            #include
            comb.append(i)
            backtrack(i + 1)

            #don't include
            comb.pop()
            backtrack(i+1)

        backtrack(1)
        return res



        