class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #one pass
        n = len(nums) #[1,2,3,5,1,2,3,4,5]
        ans = [0] * 2 * n
        
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans