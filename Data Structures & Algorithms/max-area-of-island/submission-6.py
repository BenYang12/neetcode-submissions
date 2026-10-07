class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # return max area of an island in grid
        # if no island exists, return 0
        # DFS solution

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()


        def dfs(r,c):
            # check if out of bounds, 0, or visited
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visit):
                return 0

            visit.add((r,c))

            # if cell is 1, add 1, then increment it by going in four directions
            return (1  + dfs(r + 1,c) + dfs(r - 1,c) + dfs(r,c + 1) + dfs(r,c - 1))


        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area




    
        