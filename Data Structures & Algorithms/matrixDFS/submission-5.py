class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # binary matrix Grid
        # 0 -> land
        # 1 -> untraversable rocks
        # return number of unique paths

        #DFS solution
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, visit):
            # contract of dfs -> return number of paths
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 1):
                return 0
            
            if (r == ROWS - 1 and c == COLS - 1):
                return 1

            
            # recursive backtracking part
            count = 0

            visit.add((r,c))
            count += dfs(r + 1, c, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r, c - 1, visit)
            visit.remove((r,c)) #cleanup

            return count
        
        return dfs(0,0,set())












        




            

        