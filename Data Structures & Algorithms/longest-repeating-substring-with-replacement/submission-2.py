class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #after at most K replacements -> length of ls containing only ONE distinct character
        charToCount = {} #char: number of occurrences
        L = 0
        res = 0

        for R in range(len(s)):
            charToCount[s[R]] = 1 + charToCount.get(s[R], 0)
            #expand window


            #shrink window
            while (R - L + 1) - max(charToCount.values()) > k:
                charToCount[s[L]] -= 1
                L += 1
            

            res = max(res, R - L + 1)
        return res

            
        