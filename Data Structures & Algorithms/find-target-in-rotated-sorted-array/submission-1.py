class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1


        #[1]
        while L <= R:
            mid = (L + R) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted portion
            if nums[mid] >= nums[L]:
                #search right
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1
                else:
                    #search left
                    R = mid - 1
            #right sorted portion
            else:
                #search left
                if target < nums[mid] or target > nums[R]:
                    R = mid - 1
                else:
                    L = mid + 1
            
        return -1
              




        