class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # return max area of an island in grid
        # if no island exists, return 0

        # double for-loop + DFS
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()


        def dfs(r, c):
            # contract: return area
            # base case: reject invalid/visited cells
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return 0
        

            # If we reach here, we're on a valid land cell we haven't visited
            visit.add((r,c))

            # count this cell (1) + all connected land cells from neighbors
            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) 
            return area


            
            
            

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res

        

        




    
        