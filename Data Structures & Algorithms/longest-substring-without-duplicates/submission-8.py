class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # string s -> length of longest substring w/o duplicate characters
        # TWO POINTER, SET
        # l = 0, sweep through s with r
        # add s[r] to set, if s[r] alr in set, increment l and remove s[l] from set
        # calculate max length all the time

        # s = "pwwkew"

        # TC: O(n)
        # SC: O(n)
       

        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            res = max(r - l + 1, res)
        
        return res
            


        