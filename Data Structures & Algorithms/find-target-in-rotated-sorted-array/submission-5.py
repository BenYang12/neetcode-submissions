class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #rotated sorted array nums -> return index of target or -1
        #[3,4,5,6,0,1,2] target = 0

        #left sorted portion -> target < nums[l] or target > nums[mid] -> search right
        #else search left


        #right sorted portion  -> target > nums[r] or target < nums[mid] -> go left
        #else search right


        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            
            #left sorted portion
            if nums[mid] >= nums[l]:
                #go right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                #go left
                else:
                    r = mid -1

            #right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    #go left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

            






        

        