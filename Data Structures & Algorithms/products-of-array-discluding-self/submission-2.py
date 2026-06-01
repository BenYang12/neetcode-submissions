class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #res, return value
        res = [0] * len(nums)

        #prefix array
        pre = []
        total = 1
        for num in nums:
            total *= num
            pre.append(total)


        #postfix array
        post = [0] * len(nums)
        total = 1
        for i in range(len(post) -1, -1, -1):
            total *= nums[i]
            post[i] = total

       
     

        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                res[i] = pre[i-1] * post[i+1]

            if i <= 0:
                res[i] = 1 * post[i+1]

            if i >= len(nums) - 1:
                res[i] = pre[i-1] * 1
        return res

     

        
        




        
        