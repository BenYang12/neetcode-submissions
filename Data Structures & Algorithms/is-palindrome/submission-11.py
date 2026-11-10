class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string s -> return true if palindrome
        # two pointer solution
        l, r = 0, len(s) - 1
        
        while l < r:
            # edge case: pointers going out of bounds, use while loop
            while l < r and not self.isAlpha(s[l]):
                l += 1
            
            # use while loop
            while l < r and not self.isAlpha(s[r]):
                r -= 1

            # conver to lowercase to ensure strict equality
            if s[l].lower() != s[r].lower() :
                return False
            
            l += 1
            r -= 1
        
        return True




    # Alphanumeric helper function
    def isAlpha(self, c):
        return ord("A")<= ord(c) <= ord("Z") or ord("a")<= ord(c) <= ord("z") or ord("0")<= ord(c) <= ord("9")

    

        
