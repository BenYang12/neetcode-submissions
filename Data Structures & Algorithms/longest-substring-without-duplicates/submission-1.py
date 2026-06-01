class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        charSet = set()
        L = 0
        maxLen = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L+=1
            charSet.add(s[R])
            res = R - L + 1
            maxLen = max(maxLen,res)
        return maxLen
        





            
        