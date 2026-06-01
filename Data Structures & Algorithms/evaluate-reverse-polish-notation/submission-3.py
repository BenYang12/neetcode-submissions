class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == "/":
                a,b = stack.pop(), stack.pop()
                res = int(float(b) / a)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]


     
            
            
            


        