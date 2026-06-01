class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            mid = (L + R) // 2
            res = min(nums[mid], res)


            #we are in left sorted portion
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                #we are in right sorted portion
                R = mid - 1

        return res

            

            

        