class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curComb = []
        self.helper(1, n,k, curComb, res)
        return res

    def helper(self,i, n, k, curComb,res):
        #base case
        if len(curComb) == k:
            res.append(curComb.copy())
            return

        if i > n:
            return

        
        #first choice, include
        curComb.append(i)
        self.helper(i+1, n, k, curComb,res)

        #second choice, don't include
        curComb.pop()
        self.helper(i+1, n, k, curComb,res)
        