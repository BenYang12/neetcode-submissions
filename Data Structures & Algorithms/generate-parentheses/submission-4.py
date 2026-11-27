class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # integer n -> return all well-forrmed parenthesis strings I can generate with n pairs

        # Input: n = 3
        # Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        # Backtracking -> add open, or closed
        # OpenN == ClosedN == n -> return that well formed
        # I can add open as long as OpenN < n
        # I can add closed as long as ClosedN < OpenN
        stack = []
        res = []

        def backtrack(openN, closedN):
            # base case
            if openN == closedN == n:
                res.append("".join(stack))


            # add an open -> explore that path
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()


            # add a closed -> explore that path
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
            
        return res
            
        



        
       

      
            




       




        