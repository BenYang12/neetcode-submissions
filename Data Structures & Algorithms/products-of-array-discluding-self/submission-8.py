class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums -> output where output[i] is product of all elements of nums except nums[i]


        # build prefix and suffix array
        # pref[i] =  product of all elements to the left of i
        # suff[i] = product of all elements to the right of i
        # res[i] = pref[i] * suff[i]

        res = [0] * len(nums)


        # prefix array
        pref = []
        total = 1
        for n in nums:
            total *= n
            pref.append(total)
        

        # suffix array
        suff = []
        total = 1
        for num in nums[::-1]:
            total *= num
            suff.append(total)
        suff.reverse()

        # build res array
        for i in range(len(res)):
            left = pref[i - 1] if i > 0 else 1
            right = suff[i + 1] if i < len(res) - 1 else 1
            res[i] = left * right

        return res 

        



      
        







    


    


        


        