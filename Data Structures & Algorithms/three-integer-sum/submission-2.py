class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #iterate through nums to find possible first value
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue #continue to next iteration
            
            L = i+1
            R = len(nums)-1

            while L<R:
                threeSum = a + nums[L] + nums[R] 

                if threeSum > 0:
                    R-=1
                elif threeSum < 0:
                    L+=1
                else: #valid triplet found
                    res.append([a,nums[L], nums[R]])
                    #I only have to update one pointer
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        return res

                
        