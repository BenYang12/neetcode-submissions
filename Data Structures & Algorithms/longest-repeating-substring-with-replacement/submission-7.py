class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "XYYX", k = 2
        # s = "AAABABB", k = 1

        

        # sliding window 
        # want to replace the least frequent character in the string
        # window is valid as long as len(s) - freq(most common character) <= k
        # track frequency of each char -> dict


        charCount = defaultdict(int) # {char: # occurrences of char}
        l = 0
        res = 0
        for r in range(len(s)):
            charCount[s[r]] += 1

            # invalid window, shrink
            while (r - l + 1 ) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
               

            res = max(res, (r - l) + 1)
            
        
        return res



            

            

        
        