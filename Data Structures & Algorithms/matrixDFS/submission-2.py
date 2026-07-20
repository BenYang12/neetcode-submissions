class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        #Grid, 0s represent land, 1s represent rocks -> return number of unique paths from top left to bottom right. 
        #I can move vertically or horizontally, can't visit the same path twice


        #matrix DFS
        rows, cols = len(grid), len(grid[0])
        visit = set() 
    

        def dfs(r,c, visit):
            #contract of my DFS -> return number of paths 

            #base cases
            if (min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == 1):
                return 0

            if (r == rows - 1 and c == cols - 1):
                return 1

            #recursive backtracking part
            
            visit.add((r,c)) 
            res = 0
            res += dfs(r + 1, c, visit)
            res += dfs(r - 1, c, visit)
            res += dfs(r, c + 1, visit)
            res += dfs(r, c - 1, visit)

            visit.remove((r,c)) #cleanup
            return res

        return dfs(0, 0, set())



        