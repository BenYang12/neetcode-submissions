class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open == closed == n -> append result and return 
        # open < n -> make a function call adding a (
        # closed < open -> make a function call adding a )

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack.copy()))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0,0)
        return res

            






        