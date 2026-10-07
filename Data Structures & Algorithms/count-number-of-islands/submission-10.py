class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # "1" -> land
        # "0" -> water
        # return number of islands
        # BFS solution

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
       

        def bfs(r,c):
            q = deque()
            grid[r][c] == "0"
            q.append((r,c))
            

            while q:
                r, c = q.popleft()

                # iterate through all four neighbors
                for dr, dc in directions:
                    nr,nc = r + dr, c + dc
                    if nr == ROWS or nr < 0 or nc == COLS or nc < 0 or grid[nr][nc] == "0":
                        continue

                    # land, so make this neighbor not an island anymore
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
                 
                



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        
        return islands







    

        