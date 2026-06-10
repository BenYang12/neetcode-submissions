class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer approach
        L = 0
        R = len(s) - 1

        while L < R:
            while not self.isAlpha(s[L]) and L < R:
                L += 1
            while not self.isAlpha(s[R]) and L < R:
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1

        return True

    



    def isAlpha(self, char):
        return ord("a")<= ord(char) <= ord("z") or ord("A")<= ord(char) <= ord("Z") or ord("0")<= ord(char) <= ord("9")
        