class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # return integer that represents evaluation of the expression
        # tokens = ["1","2","+","3","*","4","-"]

        # use a stack! 
        stack = []


        for token in tokens:
            if token == "+":
                new = int(stack.pop()) + int(stack.pop())
                stack.append(new)
            elif token == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                new = num2 - num1
                stack.append(new)
            elif token == "*":
                new = int(stack.pop()) * int(stack.pop())
                stack.append(new)
            elif token == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                new = int(num2 / num1 )
                stack.append(new)
            else:
                stack.append(int(token))
            
        return stack[-1]




        


        