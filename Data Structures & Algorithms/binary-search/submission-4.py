class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if target > nums[m]:
                L = m + 1
            
            elif target < nums[m]:
                R = m - 1

            else:
                return m
        return -1 
        


        