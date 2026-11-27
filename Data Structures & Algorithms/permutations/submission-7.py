class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # generate perms by building them from smaller perms
        # if list empty -> only permutation is []

        # otherwise...
        # 1. take first number of list
        # 2. recursively get all permutations of the remaining nums
        # 3. for each smaller permutation, insert first number into
        # every possible position

        # [1, 2, 3] -> [2, 3] -> [3] -> [[]]


        # base case 
        if len(nums) == 0:
            return [[]]
        

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res


        

        

        