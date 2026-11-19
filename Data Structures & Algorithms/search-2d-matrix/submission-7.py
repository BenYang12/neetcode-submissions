class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix, target -> return true if target exists, false otherwise
        # O(log(m * n)) time

        # alg:
        # 1. run binary search on rows
        # 2. run binary search on cols
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search on rows -> row where target is located
        l, r  = 0, ROWS - 1

        while l <= r:
            row = (l + r) // 2

            if target > matrix[row][COLS - 1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                break
                # after this break statement, mid = row where target is located

        
        # binary serach on target row
        l, r = 0, COLS - 1
        while l <= r:
            col = (l + r) // 2

            if target > matrix[row][col]:
                l = col + 1
            
            elif target < matrix[row][col]:
                r = col - 1
            
            else:
                return True
        return False
            
        


        