class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] == target:
                return m
            
            #left sorted portion
            if nums[m] >= nums[L]:
                if target > nums[m]:
                    #search right
                    L = m + 1
                elif target < nums[m] and target < nums[L]:
                    #search right
                    L = m + 1
                else:
                    #search L
                    R= m - 1
            #right sorted portion
            else:
                if target < nums[m]:
                    #search left
                    R = m- 1
                elif target > nums[m] and  target > nums[R]:
                    #search left
                    R = m - 1
                else:
                    L = m + 1
        return -1

               








        