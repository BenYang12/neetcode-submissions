class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #given array nums of unique integers, return all possible subsets of nums
        #solution set must not contain duplicate subsets

        curSet, subSets = [], []

        def helper(i, curSet, subSets):
            if i == len(nums):
                subSets.append(curSet.copy())
                return

            #include nums[i]
            curSet.append(nums[i])
            helper(i + 1, curSet, subSets)

            curSet.pop()

            #don't include nums[i]
            helper(i + 1, curSet, subSets)
        helper(0, curSet, subSets)
        return subSets

        
        