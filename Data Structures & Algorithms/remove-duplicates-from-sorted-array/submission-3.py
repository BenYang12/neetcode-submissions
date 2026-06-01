class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1 
        for R in range(L, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L+=1
        return L

       
        