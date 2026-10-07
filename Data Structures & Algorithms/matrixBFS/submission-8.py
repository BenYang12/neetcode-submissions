class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # Return length of shortest path from top-left to bottom-right

        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1 

        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))

        length = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                # if not at end, expand outwards in 4 directions
                neighbors = [[0,1], [0, -1],[1,0], [-1, 0]]
                for dr, dc in neighbors:
                    if r + dr == ROWS or r + dr < 0 or c + dc == COLS or c + dc < 0 or (r + dr,c + dc) in visit or grid[r + dr][c+dc] == 1:
                        continue
    
                    visit.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
            length += 1
        return -1