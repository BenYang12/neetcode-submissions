class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return length of longest substring

        # Input: s = "ABAB", k = 2
        # Output: 4


        # Input: s = "AABABBA", k = 1
        # Output: 4

        # sliding window -> condition for validity is len(window) - frequency of most common char <= k

        # TC: O(n)
        # SC: O(n)

        count = {} # char: freq of char
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res
            







        