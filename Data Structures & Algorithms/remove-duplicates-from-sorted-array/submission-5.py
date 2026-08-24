class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # compare each elem w/ predecessor.
        # duplicates are consecutive in sorted array, so element is unique
        # if it differs from one before it. 

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                #unique
                nums[l] = nums[r]
                l += 1
        return l
            





            






        