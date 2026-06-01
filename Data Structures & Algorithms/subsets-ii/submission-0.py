class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #non distinct elements, with duplicates
        #sort first
        nums.sort()
        subSets = []
        curSet = []

        self.helper2(0,nums,curSet, subSets)
        return subSets

    def helper2(self, i, nums,curSet, subSets):
        #base case
        if i >= len(nums):
            subSets.append(curSet.copy())
            return
        
        #choice 1, include
        curSet.append(nums[i])
        self.helper2(i + 1, nums, curSet, subSets)

        #choice 2, don't include, remember nums may include duplicates
        curSet.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper2(i + 1, nums,curSet, subSets)
        

        
        