class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #given array nums of unique integers -> return all possible permutations
        
        #base case
        if len(nums) == 0:
            return [[]]
        

        #recursive case
        #keep calling recursive function with the input nums, WITHOUT the first element
        perms = self.permute(nums[1:])

        #then, add current element to all of these at every possible permutation
        res = []
        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j,nums[0])
                res.append(p_copy)
        return res



        




        