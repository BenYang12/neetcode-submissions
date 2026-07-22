class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #grid -> return max area of island in grid (no island return 0)
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            # contract: return the area

            #base cases
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visit or grid[r][c] == 0:
                return 0
                
            visit.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) )
        
       

        #iterate through the entire grid -> see a one -> DFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    res = max(res, dfs(r,c))


        return res

        

            

        
            


