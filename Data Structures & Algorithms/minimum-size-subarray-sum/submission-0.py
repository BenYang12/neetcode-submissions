class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumSum = 0
        L = 0
        minLength = float('inf')

        for R in range(len(nums)):
            cumSum += nums[R] 

            while cumSum >= target:
                length = (R - L) + 1
                minLength = min(length, minLength)
                cumSum -= nums[L]
                L += 1
            
        
        
        return 0 if minLength == float('inf') else minLength


 

       