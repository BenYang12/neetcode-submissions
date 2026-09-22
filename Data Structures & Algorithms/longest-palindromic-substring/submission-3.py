class Solution:
    def longestPalindrome(self, s: str) -> str:
        # given string s, return longest palindromic substring

        # s = ababc
        # output = bab


        # Brute force: n^2 substrings -> n to check each substring -> O(n^3)
        # DP: If we compare the first and the last character and they are equal, the sub-problem is     determining whether the inner string, excluding the characters at index 0 and length - 1, is a palindrome. if inner string is palindrome, so are the outer most characters
        
        # iterate through every single char -> e, then expand outward
        # handle edge case of even length substrings

        res = ""
        length = 0


        # odd case
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r - l + 1)
                    res = s[l: r + 1]
                l -= 1
                r += 1

        # even case
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r - l + 1)
                    res = s[l: r + 1]
                l -= 1
                r += 1
        return res






        
        