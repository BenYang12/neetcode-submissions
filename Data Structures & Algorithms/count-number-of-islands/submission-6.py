class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Grid -> return number of islands
        #Iterate through entire grid, when ever I reach one, use BFS to eliminate all adjacent ones 
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set() #visit should stay global
        

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
           

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    neighbors = [[0,1], [0,-1],[1,0], [-1,0]]
                    for dr, dc in neighbors:
                        if min(r + dr,c + dc) < 0 or (r + dr) == rows or (c + dc) == cols or grid[r + dr][c + dc] == "0" or (r + dr, c + dc) in visit:
                            continue
                        visit.add((r + dr,c + dc))
                        q.append((r + dr, c + dc))

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    res += 1
                    bfs(r,c)
        return res


            
        