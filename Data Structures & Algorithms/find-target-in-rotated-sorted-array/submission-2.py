class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # nums = [3,4,5,6,1,2], target = 1
        #Binary Search

        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[L]:
                #we are in the left sorted portion
                if target > nums[mid] or target < nums[L]:
                    #search right
                    L = mid + 1
                else:
                    R = mid - 1 
            else:
                #we are in the right sorted portion
                if target < nums[mid] or target > nums[R]:
                    #go left
                    R = mid - 1
                else:
                    #go right
                    L = mid + 1
        return -1 









        