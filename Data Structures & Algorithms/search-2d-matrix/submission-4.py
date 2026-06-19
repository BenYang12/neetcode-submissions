class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                arr.append(matrix[row][col])

        L = 0
        R = len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid - 1
            else:
                return True
        return False
        
        