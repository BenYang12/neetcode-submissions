class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sorted_list = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                sorted_list.append(matrix[r][c])
            

        #run binary search on sorted_list

        L = 0
        R = len(sorted_list) - 1

        while L <= R:
            m = (L + R) // 2

            if target > sorted_list[m]:
                L = m + 1
            
            elif target < sorted_list[m]:
                R = m - 1
            
            else:
                return True
        return False
                

        