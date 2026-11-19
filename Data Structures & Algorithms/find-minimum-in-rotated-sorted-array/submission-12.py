class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2], all elements unique
        # return minimum element in O(logn) time


        # Binary Search!


        # l = 0
        # r = len(nums) - 1
        # calculate mid

        # if nums[mid] >= nums[l] -> mid in left sorted portion, search right sorted portion!
        # else -> mid in right sorted portion, keep searching left!


        res = float("inf")
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])


            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                # in left sorted portion -> search right!
                l = mid + 1
            else:
                # in right sorted portion -> keep going left!
                r = mid - 1
        return res
            

            



        


        