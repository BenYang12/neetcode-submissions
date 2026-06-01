class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #one pass with a hashmap
        
        seen = {} #number, number index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        
        
        