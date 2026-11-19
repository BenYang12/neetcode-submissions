class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rotated sorted array nums, integer target, return index of target or -1
        # O(logn) -> BINARY SEARCH

        # nums = [3,4,5,6,1,2], target = 1

        # left sorted portion:
        # 1. target < nums[l] or target > nums[m]  -> search right
        # 2. else -> search left


        # right sorted portion:
        # 1. target > nums[r] or target < nums[m] -> search left 
        # 2. else -> search right

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[m] >= nums[l]:
                # left sorted portion
                if target < nums[l] or target > nums[m]:
                    # go right
                    l = m + 1
                else:
                    # go left
                    r = m - 1

            else:
                # right sorted portion
                if target > nums[r] or target < nums[m]:
                    # go left
                    r = m - 1
                else:
                    # go right
                    l = m + 1
        return -1 



















      

       

       





        

        