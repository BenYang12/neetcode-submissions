class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        #given binary matrix Grid -> return number of unique paths from top left corner of grid to the bottom-right corner
        #backtracking -> using recursive dfs
        #need a set to keep track of stuff i alr visited

        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, r, c, visit):
            #base case 1
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == 1:
                return 0
            
            #base case 2
            if r == rows - 1 and c == cols - 1:
                return 1

            
            visit.add((r,c))
            count = 0
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)

            #backtracking part
            visit.remove((r,c))
            return count

        return dfs(grid,0,0,set())



            





        