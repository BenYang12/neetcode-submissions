class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        #given binary matrix Grid, 0s represent land and 1s represent rocks
        #return number of unique paths from top-left corner to bottom-right
        #confused about return var count , define it after adding to set
        rows = len(grid)
        cols = len(grid[0])


        def dfs(grid, r,c,visit):
            #base case
            if (min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == 1):
                return 0
            
            #base case
            if (r == rows - 1 and c == cols - 1):
                return 1

            
            #recursive backtracking part
            visit.add((r,c))
            count = 0
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r , c + 1, visit)
            count += dfs(grid, r , c - 1, visit)

            visit.remove((r,c))
            return count
        
        return dfs(grid,0,0,set())




        
        