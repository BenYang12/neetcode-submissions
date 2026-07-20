class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors: 
                    if (r + dr < 0 or  c + dc < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == -1):
                        continue
                    q.append((r + dr,c + dc))
                    visit.add((r + dr,c + dc))
            dist += 1
        
        
            
        
        