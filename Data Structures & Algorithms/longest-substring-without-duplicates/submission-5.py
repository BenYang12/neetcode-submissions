class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        L = 0
        seen = set()

        for R in range(len(s)):
            #check validity/shrink window
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            
            seen.add(s[R])
            max_length = max(max_length, R - L + 1)
            

        return max_length
                


        