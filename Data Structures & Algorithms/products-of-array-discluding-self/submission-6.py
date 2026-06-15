class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        #build prefix array
        total = 1
        prefix = []
        for n in nums:
            total *= n
            prefix.append(total)

        #build postfix array
        total = 1
        postfix = []
        for n in nums[::-1]:
            total *= n
            postfix.append(total)
        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                res[i] = 1 * postfix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i-1] * 1
            else:
                res[i] = postfix[i + 1] * prefix [i - 1]
        return res







    
            

        