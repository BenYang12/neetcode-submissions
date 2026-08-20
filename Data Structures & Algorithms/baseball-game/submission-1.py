class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #stack 
        stack = []

        for char in operations:
            if char == "+":
                first, second = int(stack[-1]), int(stack[-2])
                stack.append(first + second)
            elif char == "D":
                new_score = int(stack[-1])
                stack.append(new_score * 2)
            elif char == "C":
                stack.pop()
            else:
                stack.append(int(char))

        res = 0
        for n in stack:
            res += n
        return res

        



        