class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0] * len(nums)

        #build prefix
        pre = []
        total = 1
        for n in nums:
            total *= n
            pre.append(total)

        
        #build postfix
        post = []
        total = 1
        for n in reversed(nums):
            total *= n
            post.append(total)
        post.reverse()

        for i in range(len(nums)): 
            if i > 0:
                left = pre[i-1]
            else:
                left = 1
            
            if i < len(nums) - 1:
                right = post[i + 1]
            else:
                right = 1
            

            output[i] = right * left
        return output





        

        