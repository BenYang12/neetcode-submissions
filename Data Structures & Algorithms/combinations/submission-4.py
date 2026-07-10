class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        curComb, combs = [], []

        def dfs(i, curComb, combs, n, k):

            #base case
            if len(curComb) == k:
                combs.append(curComb.copy())
                return 

            if i > n:
                return

            #include i 
            curComb.append(i)
            dfs(i + 1, curComb, combs, n, k)

            #don't include nums[i]
            curComb.pop()
            dfs(i + 1, curComb, combs, n, k)
        dfs(1, curComb, combs, n, k)
        return combs
        
            
        