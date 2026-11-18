class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "XYYX", k = 2
        # s = "AAABABB", k = 1

        

        # sliding window 
        # want to replace the least frequent character in the string
        # window is valid as long as len(s) - freq(most common character) <= k
        # track frequency of each char -> dict


        # TC: O(n)
        # SC: O(n)


        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(count.values())

            while (r - l + 1 ) - maxf > k:
                # count[s[l]] is guaranteed to exist  b/c l only ever points to a char thats inside current window, and every character in the window has already been added to count when the right pointer passed over it!
                count[s[l]] -= 1
                l += 1
        

            res = max(res, (r - l + 1))
        return res


            

            

        
        