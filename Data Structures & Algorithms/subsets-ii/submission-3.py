class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort to skip over duplicates
        curSet, subSets = [], []

        def helper(i, curSet, subSets):
            if i >= len(nums):
                subSets.append(curSet.copy())
                return

            
            #include nums[i]
            curSet.append(nums[i])
            helper(i + 1, curSet, subSets)

            curSet.pop()


            #don't include nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            helper(i + 1, curSet, subSets)

        helper(0, curSet, subSets)

        return subSets

        