class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #XYYK -> after at most k replacements, return length of longest substring which contains only one distinct character
        res = 0
        charToCount = {} #character: count
        L = 0

        for R in range(len(s)):
            charToCount[s[R]] = 1 + charToCount.get(s[R], 0)
            
            while (R - L + 1) - max(charToCount.values()) > k:
                charToCount[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)
        return res
            
        
    
        