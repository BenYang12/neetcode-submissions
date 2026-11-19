class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix, target -> return true if target exists, false otherwise
        # O(log(m * n)) time

        # alg:
        # 1. run binary search on rows
        # 2. run binary search on cols
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search on rows -> row where target is located
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bot = row - 1
            
            else:
                # terminate loop, row ends at row where target is located
                break
        
        if not (top <= bot):
            return False
        

        # binary serach on target row
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        
        


        