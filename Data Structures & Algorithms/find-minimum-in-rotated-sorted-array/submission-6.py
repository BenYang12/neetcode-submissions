class Solution:
    def findMin(self, nums: List[int]) -> int:
        #sorted rotated array -> minimum value
        #O(logn) -> binary search

        L = 0
        R = len(nums) - 1
        res = nums[0]

        while L <= R:

            if nums[L] <= nums[R]:
                res = min(res, nums[L])
                break
                

            #if nums[L] is not less than or equal to nums[R], then the portion we have is not sorted, and the pivot is still active
            mid = (L + R) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[L]:
                #we are in left sorted portion -> go right
                L = mid + 1
            
            else:
                #we are in right sorted portion -> keep searching left
                R = mid - 1
        return res
            
        
        
        