class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sorted_list = []
        for row in matrix:
            for elem in row:
                sorted_list.append(elem)

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
                

        