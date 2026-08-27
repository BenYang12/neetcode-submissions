class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #return number of possible unique paths that can be taken from top-left corner to bottom right


        bottom_row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n

            #last col is always 1
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + bottom_row[j]

            bottom_row = newRow
        return bottom_row[0]
            


        