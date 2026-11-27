class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs of parenthesis -> generate all combinations of well-formed parentheses



        # n = 3, 6 total (3 open, 3 closed)
        # 3 open, 3 closed -> valid (base case)
        # can add up to 3 open parenthesis
        # can only add closing parenthesis if closeCount < openOpenCount


        # backtracking (DFS)
        # only add open parenthesis if open < n
        # only add closing parenthesis if closed < open
        # valid IFF open == closed == n 

        stack = []
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

      
            




       




        