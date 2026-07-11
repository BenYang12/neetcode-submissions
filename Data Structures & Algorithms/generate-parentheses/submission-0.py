class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add closing parenthesis if closed < open
        #valid IIF only == closed == n


        stack = [] #holds parenthesis
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
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

            

            

        