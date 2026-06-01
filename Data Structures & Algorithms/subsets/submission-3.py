class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []
        

        #Backtracking -> Recursive DFS with a twist ("Undo")
        def helper(i, curSet, nums):

            #base case
            if i >= len(nums):
                res.append(curSet.copy())
                return

            
            #first choice, include
            curSet.append(nums[i])
            helper(i + 1, curSet, nums)

            #second choice, don't include
            curSet.pop()
            helper(i + 1, curSet, nums)

        helper(0, curSet, nums)
        return res





        
        