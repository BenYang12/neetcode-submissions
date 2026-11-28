class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Input: m x n matrix containing 'X' and 'O'
        # Capture all regions that are 4-directionally surrounded by X

        # Reverse Thinking: 
        # - "Give me only A" == "Give me everything except B"
        # - "Capture surrounded regions" == "Capture everything except unsurrounded regions"

        # region connected to border -> unsurrounded


        # Alg:
        # scan through cells looking for unsurrounded Os
        # use DFS to change O to T
        # scan through again, O -> X, T -> O
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            # base case: out of bounds
            if min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1,c)
            capture(r - 1,c)
            capture(r,c + 1)
            capture(r,c - 1)




        # 1. (DFS) Find Unsurrounded regions -> convert to T
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O") and (r in [0, ROWS - 1]) or (c in [0, COLS - 1]):
                    capture(r,c)


        # 2. Capture surrounded Regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
                

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"



        