class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m x n grid -> return number of islands
        # islands connected by adjacent lands horizontally or vertically (no diagonal connections)

        # double for-loop + BFS
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            q = deque()
            visit = set()
            q.append((r,c))
            visit.add((r,c))
            grid[r][c] == "0"
            

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] == "0":
                            continue
                        
                        grid[nr][nc] = "0"
                        q.append((nr,nc))
                        visit.add((nr,nc))

            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        
        return res
        
        