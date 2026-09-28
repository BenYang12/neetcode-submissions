class Solution:
    def longestPalindrome(self, s: str) -> str:
        # given string s -> return longest substring of s that is palindrome
        # s = ababd
        # brute force: O(n^3)


        # expand from middle to bring down to O(n^2)
        # s = "ababd"

        length = 0
        res = ""

        # odd palindromic substrings
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r - l + 1)
                    res = s[l:r + 1]
                
                l -= 1
                r += 1

        # even palindromic substrings
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1
        
        return res


        
        