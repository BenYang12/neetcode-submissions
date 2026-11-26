class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # rotated array nums, integer target -> return idx of target, or -1
        # Input: nums = [4,5,6,7,0,1,2], target = 0
        # Output: 4

        # O(logn) -> Binary Search
        # Binary search alg

        # [4,5,6,7,0,1,2]
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                # left sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
        return -1 






        