class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L = 0
        R = len(nums) - 1

        while L <= R:
            #we run into a sub array that is already sorted
            if nums[L] < nums[R]:
                res = min(res,nums[L])
                break
            

            #if array is not sorted
            m = (L + R) // 2
            res = min(res, nums[m])

            #search left or search right?
            if nums[m] >= nums[L]:
                #search right
                L = m + 1
            else:
                #in right sorted portion
                R = m - 1
        return res



 

        