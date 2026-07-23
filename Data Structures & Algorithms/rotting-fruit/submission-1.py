class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #matrix -> minimum number of minutes that must elapse until no more fresh fruits
        #if impossible -> return -1 

        #DFS fails to account for the fact that I need to run simultaneously from ALL rotten oranges
        #BFS from rotten fruits -> O(m*n)

        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        #all rotten fruits queued up -> simultaneous bfs
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                
                

                neighbors = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    nr,nc = r + dr, c + dc
                    if nr == rows or nc == cols or nr < 0 or nc < 0 or (nr,nc) in visit or grid[nr][nc] != 1:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
                    fresh -= 1
            time += 1
        
        return time if not fresh else -1
                
                    


        