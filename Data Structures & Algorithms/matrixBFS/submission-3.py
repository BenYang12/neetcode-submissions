class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #grid -> length of shortest path from top left to bottom right
        #matrix bfs -> implement a set and a queue
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        q.append((0,0))
        visit.add((0,0))


        length = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr,dc in neighbors:
                    if min(r + dr, c + dc) < 0 or (r + dr, c + dc) in visit or r + dr == rows or c + dc == cols or grid[r + dr][c + dc] == 1:
                        continue
                    
                    q.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
                
            length += 1
        
        return -1

                

            


    
        