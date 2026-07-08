class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper(i, curComb, combs, n, k ):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            
            if i > n:
                return

            

            #include i in combination
            curComb.append(i)
            helper(i + 1, curComb, combs, n,k)


            curComb.pop()

            #don't include i in combination
            helper(i + 1, curComb, combs, n, k)

        helper(1, [], combs, n,k)

        return combs
        
        


        
        