class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #num, target,  => return i and j such that nums[i] + nums[j] == target, i !=j
        #for num, other number = target - num => I'll create a hashmap for all numbers and look for this diff

        seen = {} #num: index

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]
            
            seen[num] = i
            



        