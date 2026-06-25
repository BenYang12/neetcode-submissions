class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums -> output where output[i] is product of all elements of nums except nums[i]
        #build prefix and postfix array
        res = [0] * len(nums)

        #build prefix array
        pre = []
        total = 1
        for n in nums:
            total *= n
            pre.append(total)

        #build postfix array
        post = []
        total = 1
        for n in nums[::-1]:
            total *= n
            post.append(total)
        post.reverse()

        for i in range(len(nums)):
            left = pre[i - 1] if i > 0 else 1
            right = post[i + 1] if i < len(nums) - 1 else 1
            res[i] = left * right

        return res







    


    


        


        