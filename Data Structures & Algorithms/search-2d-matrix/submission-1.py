class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        big_arr = []

        for row in matrix:
            for item in row:
                big_arr.append(item)

        L = 0
        R = len(big_arr) - 1

        while L <= R:
            mid =(L + R) // 2

            if target > big_arr[mid]:
                L = mid + 1
            elif target < big_arr[mid]:
                R = mid - 1
            else:
                return True
        return False
            
        

    
        