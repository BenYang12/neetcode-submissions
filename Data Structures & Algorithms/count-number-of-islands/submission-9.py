class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # "1" -> land
        # "0" -> water
        # return number of islands
        # BFS solution


        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = set()
        q = deque()

        def bfs(r,c):
            visit.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]

                # iterate through all four neighbors
                for dr, dc in neighbors:
                    if r + dr == ROWS or r + dr < 0 or c + dc == COLS or c + dc < 0 or (r + dr, c + dc) in visit or grid[r + dr][ c + dc] == "0":
                        continue

                    # make this neighbor not an island anymore
                    grid[r + dr][c + dc] = "0"
                    q.append((r+dr, c + dc))
                    visit.add((r + dr, c + dc))
                



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        
        return res







    

        