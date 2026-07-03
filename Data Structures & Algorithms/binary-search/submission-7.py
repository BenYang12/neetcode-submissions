class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #search for target within nums -> return index if found, otherwise -1 
        #O(logn) -> binary search algorithm 

        l = 0 
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid + 1
            
            elif target < nums[mid]:
                r = mid - 1
        return -1
        


        