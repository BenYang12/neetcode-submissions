class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = [0] * len(nums)


        #build prefix array
        total = 1
        for n in nums:
            total *= n
            prefix.append(total)

        #build postfix array
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            postfix.append(total)
        postfix.reverse()

     

        for i in range(len(nums)):
            if i > 0:
                left = prefix[i - 1]
            else:
                left = 1
            
            if i < len(nums) - 1:
                right = postfix[i+1]
            else:
                right = 1
            
            output[i] = right * left
            
        return output

                





        