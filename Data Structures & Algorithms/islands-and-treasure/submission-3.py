class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #mxn grid 
    
        #brute force/naive -> for every empty cell, try to find shortest path to any treasure using DFS -> O(n*m)^2
        #BFS perfect for shortest path in an unweighted grid 
        # -> 1. from every empty cell, we expand level-by-level -> lots of repeated work 
        # -> 2. from every gate, expand level-by-level -> simultaneously -> O(m * n)

        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        # I now have treasure chests appended in the queue
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance

                neighbors = [[1,0], [-1,0], [0,1], [0, -1]]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr,nc) in visit or grid[nr][nc] == -1:
                        continue

                    visit.add((nr,nc))
                    q.append((nr,nc))
            distance += 1
        
                   

                    


                                                        