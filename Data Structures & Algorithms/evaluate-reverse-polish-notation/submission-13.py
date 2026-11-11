class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # return integer that represents evaluation of the expression
        # tokens = ["1","2","+","3","*","4","-"]

        # use a stack! 
        stack = []


        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
                
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/float(a)))
                
            else:
                stack.append(int(c))
            
        return stack[-1]




        


        