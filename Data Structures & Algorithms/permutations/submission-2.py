class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #base case
        if len(nums) == 0:
            return [[]]


        #recursive case aka subproblem
        perms = self.permute(nums[1:])

        #return value up the call stack
        res = []

        #iterate through every permutation, then iterate through every index we can insert
        for perm in perms:
            for j in range(len(perm) + 1):
                #create a copy of perm because I can possibly use it multiple times
                perm_copy = perm.copy()
                perm_copy.insert(j, nums[0])
                res.append(perm_copy)

        return res


        