class Solution:
    def countSubstrings(self, s: str) -> int:
        # given string s, return number of substrings within s that are palindromes
        # s = "abba", output = 3


        # alg -> iterate through s, expand each char outwards
        # every time we expand and maintain palindromic constraints -> increment global counter


        # expanding from middle optimizes from O(n^3) -> O(n^2)

        res = 0

        # odd substrings
        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        # even substrings
        for i in range(len(s)):
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
        