class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #my solution must run in O(logn)
        #sorted
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2 #potential overflow

            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        return -1






      

        