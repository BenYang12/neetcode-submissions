class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]":"["}
        for char in s:
            if stack and char in closeToOpen:
                if stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False


        