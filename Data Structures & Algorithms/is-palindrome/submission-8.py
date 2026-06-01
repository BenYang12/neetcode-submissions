class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two pointer Solution, L at start and R at end
        #Case insensitive + ignore all non-alphanumeric characters
        L = 0
        R = len(s) - 1

        while L < R:

            while L < R and not self.isAlpha(s[L]):
                L += 1
            
            while L < R and not self.isAlpha(s[R]):
                R -= 1
            
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True



    def isAlpha(self, c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")) 

        