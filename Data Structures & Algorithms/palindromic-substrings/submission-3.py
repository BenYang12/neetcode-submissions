class Solution:
    def countSubstrings(self, s: str) -> int:
        # string s -> return number of substrings within s that are palindromes

        count = 0

        #odd
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
        #even
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
                
        return count



        