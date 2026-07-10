class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #base case
        if len(nums) == 0:
            return [[]]

        #recursive case -> keep calling permute with input nums, but exclude the first element
        perms = self.permute(nums[1:])

        #then add current element to all of these permutations at every possible permutation, and return it up the function call stack
        res = []
        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[0])
                res.append(p_copy)
        return res
      
                
        