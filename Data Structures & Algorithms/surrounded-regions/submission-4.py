class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #mxn matrix -> capture surrounded regions (replace all Os with Xs in-place)
        

        #Give me piece A, or Give me everything BUT piece B
        #capture the surrounded regions, capture everything BUT the unsurrounded regions
        #TC -> O(m * n)

        rows, cols = len(board), len(board[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == "O":
                    q.append((r,c))
                    visit.add((r,c))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in neighbors:
                    nr,nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr,nc) in visit or board[nr][nc] == "X":
                        continue
                    visit.add((nr,nc))
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit:
                    board[r][c] = "X"



                    
                    


    
        


                
