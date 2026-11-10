class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all triplets s.t. sum = 0
        res = []


        # sort array to ascending 
        # -4, -1, -1, 0, 1, 2
        nums.sort()

        # iterate through every single index
        # use two pointer for "rest" -> determine i and j


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]

                if threeSum > 0:
                    k -= 1
                
                elif threeSum < 0:
                    j += 1
                
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    res.append(triplet)
                    
                    k -= 1
                    j += 1
                    while j < k and  nums[j] == nums[j - 1]:
                        j += 1
                  
                    
        return res


            

            
        