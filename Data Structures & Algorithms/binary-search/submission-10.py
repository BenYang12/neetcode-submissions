class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums (sorted in ascending order), target
        # search for target within nums, return its index if exists, else -1

        # Binary Search!
        # TC: O(logn), SC:O(1)

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            
            elif target < nums[mid]:
                r = mid - 1
            
            else:
                return mid
        return -1





        
        