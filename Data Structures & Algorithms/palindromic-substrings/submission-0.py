class Solution:
    def countSubstrings(self, s: str) -> int:
        # string s -> return number of substrings within s that are palindromes
        # iterate through every character of s, expand outwards, if palindrome detected, increment res value
        #handle even and odd palindrome substring lengths
        res = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
            



        