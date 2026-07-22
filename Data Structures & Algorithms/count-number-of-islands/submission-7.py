class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #grid -> count and return the number of islands
        #iterate through entire graph, and whenever we run into a 1, increment the number islands count, and use BFS to completely "destroy the island"
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        #data structures for BFS:
        visit = set()

        def bfs(r,c):
            q = deque()

            visit.add((r,c))
            q.append((r,c))

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()


                    neighbors = [[1,0], [-1, 0], [0, 1], [0,-1]]
                    for dr, dc in neighbors:
                        row = r + dr
                        col = c + dc
                        if row < 0 or col < 0 or row == rows or col == cols or (row, col) in visit or grid[row][col] == "0":
                            continue
                        
                        q.append((row, col))
                        visit.add((row,col))



                   

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    res += 1
                    bfs(r,c) #use bfs to destroy all 1s connected to this 1 (island)

        return res




        