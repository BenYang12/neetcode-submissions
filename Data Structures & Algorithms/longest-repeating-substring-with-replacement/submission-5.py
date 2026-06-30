class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {} #char:number of occurrences
        res = 0

        for R in range(len(s)):
            #expand then shrink/check validity
            count[s[R]] = 1 + count.get(s[R],0)

            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            
            
            res = max(res, R - L + 1)
        return res

            




            
                




        

        
        