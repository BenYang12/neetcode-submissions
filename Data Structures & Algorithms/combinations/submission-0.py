class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            #base case, stop when len(comb) == k
            if len(comb) == k:
                res.append(comb.copy()) #copy() because comb is an object and b/c we can continue modifying it other recursive calls
                return
            
            #make decisions
            for i in range(start, n + 1):
                #include i
                comb.append(i)
                backtrack(i+1, comb)

                #skip i happens by finishing that recursive call, popping, and continuing the loop to the next i
                # loop continues -> effectively "skip i, try i+1"
                comb.pop()
        backtrack(1,[])
        return res
        



        