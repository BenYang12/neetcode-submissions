class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #nums, target -> minimal length of a subarray whose sum >= target
        L = 0
        minLength = float("inf")
        curSum = 0

        for R in range(len(nums)):
            curSum += nums[R]

            while curSum >= target:
                minLength = min(minLength, R - L + 1)
                curSum -= nums[L]
                L += 1
            

        if minLength != float("inf"):
            return minLength
        else:
            return 0


        
