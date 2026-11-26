class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Iteration: use idea of subproblems
        # start with one empty permutation: []

        # for every number in nums, take all existing permutations
        # and insert the new number into every possible position
        
        # [1, 2, 3]
        # 1. []
        # 2. [1]
        # 3. [[2, 1], [1, 2]]
        # 4. [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]
        perms = [[]]

        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms



        
        