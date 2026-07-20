class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #matrix Grid -> return length of shortest path from top-left to bottom-right
        rows = len(grid)
        cols = len(grid[0])

        #BFS also requires two additional data structures -> queue, set
        q = deque()
        visit = set()

        res = 0
        q.append((0,0))
        visit.add((0,0))


        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return res

                #not like DFS where I can immediately go into base cases, need helper array
                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visit or grid[r + dr][ c + dc] == 1:
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            res += 1
        return -1
    




        