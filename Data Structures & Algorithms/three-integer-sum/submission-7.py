class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort in ascending order
        res = []
        nums.sort()

        #return all triplets where nums[i] + nums[j] + nums[k] == 0
        #i,j,k should be distinct, and output should not include any duplicate triplets
        #instead of a triple loop, iterate through nums for a, then use two pointer solution to see if b and c exist that sum up to 0
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:
                threeSum = a + nums[L] + nums[R]

                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([nums[L],nums[R],a])
                    #need to update pointers
                    #[-2,-2,0,0,2,2]
                    #to prevent duplicates, I only need to shift one pointer, each value has one corresponding diff that can sum to target
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res

                    




            
           




        