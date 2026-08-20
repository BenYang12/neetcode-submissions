class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 -> [-1]
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n ) #[-1, 8]
            currMin = min(tmp, n * currMin, n ) #[-1, -8]
            res = max(res, currMax)
        return res

        