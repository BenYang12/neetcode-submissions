class Solution:
    def isValid(self, s: str) -> bool:
        #create hashmap to map open and close
        closeToOpen = {")": "(", "}": "{", "]":"["}

        #use a stack, whenever I run into a closing parenthesis, opening parenthesis should be at top of stack to ensure 1, 2, and 3
        #if stack is empty,then I can return True
        stack = []

        for char in s:
            #case 1, run into a closed parenthesis
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            #case 2 -> run into an opening parenthesis

            #DON"T FORGET THIS ELSE STATEMENT
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False

            
                

        