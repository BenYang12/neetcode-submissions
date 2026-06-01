class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #value: index
        for i,j in enumerate(nums):
            difference = target - j
            if difference in seen:
                return [seen[difference],i]
            seen[j] = i 


        