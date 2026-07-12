class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #input is array of unique integers -> return all possible subsets
        #in subsets, order does not matter

        cur, subsets = [], [] 


        def dfs(i):
            #base case
            if i >= len(nums):
                subsets.append(cur.copy())
                return

            
            #include case
            cur.append(nums[i])
            dfs(i + 1)


            #don't include case
            cur.pop()
            dfs(i + 1)
        
        dfs(0)
        return subsets


        


        
