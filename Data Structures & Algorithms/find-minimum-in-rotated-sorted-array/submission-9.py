class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")

        #[3,4,5,6,1,2]

        

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break


            mid = (l + r) // 2
            res = min(res,nums[mid])

            #if we are in left sorted portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            #if we are in right sorted portion
            else:
                r = mid - 1
        return res

            




        