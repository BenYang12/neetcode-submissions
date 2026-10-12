class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums, target -> return (i,j) s.t. nums[i] + nums[i] == target and i != j

        prevMap = {} # number: index
        
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff],i]
            else:
                prevMap[n] = i
        

            



        