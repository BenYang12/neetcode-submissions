class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        res = nums[0]


        while L <= R:
            #subarray that is already sorted
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            
            #if array is not sorted, check if we are in the left or right portion

            m = (L + R ) // 2
            res = min(res, nums[m])

            #if we are in left sorted portion, check right
            #if we are in right sorted portion, keep checking left for something thats smaller
            if nums[m] >= nums[L]:
                L = m + 1
            else:
                R = m - 1
        return res


                
        