class Solution:
    def isValid(self, s: str) -> bool:
        # return true if s is a valid string, false otherwise

        # s = "[]", true
        # s = "([{}])", true
        # s = "[(])", false


        # LIFO -> last open bracket in needs to be closed first
        # stack -> LIFO -> implemenet with dynamic array!

        # TC: O(n)
        # SC: O(n)
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in closeToOpen:
                # closing parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # opening parenthesis
                stack.append(c)
        
        return True if not stack else False


        

        


        