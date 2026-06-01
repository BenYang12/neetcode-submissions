class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "}": "{", "]":"["}
        stack = []

        for char in s:
            if char in closeToOpen:
                #if closing parenthesis
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                #open parenthesis
                stack.append(char)
        if not stack:
            return True
        else:
            return False

        