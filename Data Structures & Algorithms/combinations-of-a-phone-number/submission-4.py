class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # return all possible letter combinations that digits could represent
        # return answer in any order
        # Input: digits = "34"
        # Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

        # each digit maps to set of chars
        # choose one character per digit, in order, and generate all possible combinations

        # Backtracking
        # decision tree problem:
        # 1. Each level -> one digit
        # 2. Each Branch -> one possible character for that digit

        # TC: O(4^n * n)

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
        
        return res


        

        

        




      
    
        
      


