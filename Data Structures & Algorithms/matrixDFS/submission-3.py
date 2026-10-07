class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # binary matrix Grid
        # 0 -> land
        # 1 -> untraversable rocks
        # return number of unique paths

        #DFS solution
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c, visit):
            # contract -> return paths

            # base cases
            # 1. out of bounds/untraversable
            if r == ROWS or c == COLS or min(r,c) < 0 or (r,c) in visit or grid[r][c] == 1:
                return 0
            # 2. if we reached the end -> return 1
            if r == ROWS - 1 and c == COLS - 1:
                return 1


            #backtracking
            visit.add((r,c))
            count = 0
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r , c + 1, visit)
            count += dfs(grid, r, c - 1, visit)
            visit.remove((r,c))

            return count
        return dfs(grid, 0, 0, set())







        




            

        