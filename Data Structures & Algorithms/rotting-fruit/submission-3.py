class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS -> need a queue and a set 
        q = deque()
        visit = set()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c)) #if I see a rotten fruit, append it to the queue
                    visit.add((r,c))

        #run BFS while loop, run BFS while the q is nonempty and while we still have fresh fruits
        # q contains rotten oranges that are ready to spread
        # even if the queue still has items, if fresh == 0 we already know all fresh oranges are rotten
        #continuing loop would just waste time processing useless spreads (and incorrectly increment time)
        #thus, this statement is mandatory to break early to return the correct (minimum minutes)
        while q and fresh > 0:
            for i in range(len(q)): 
                r,c = q.popleft()

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    # if it is an in bounds fresh fruit, make it rotten
                    if (nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != 1 or (nr, nc) in visit):
                        continue

                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    visit.add((nr,nc))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1 
        