class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #grid -> return max area of an island
        #iterate through the entire grid -> 1 -> use DFS to calculate the max area
        rows, cols = len(grid), len(grid[0])
        visit = set()
        

        def dfs(r,c):
            #base case
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r,c))
            return (1 + dfs(r + 1,c) + dfs(r - 1,c) + dfs(r,c - 1) + dfs(r,c + 1))
            

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r,c))
        
        return res



        