class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #index 1 and index 2 cannot be equal => may not use the same element twice
        #solution must use O(1) additional space
        #Classic Two Pointer  (While L < R)

        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] == target:
                return [L + 1,R + 1]
            
            if numbers[L] + numbers[R] >= target:
                R-=1

            if numbers[L] + numbers[R] < target:
                L+=1

            

           
    
        