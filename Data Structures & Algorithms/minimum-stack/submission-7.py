class MinStack:

    #stacks -> dynamic arrays in python

    def __init__(self):
        self.stack = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        if not self.minstack:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            if val <= self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
            self.stack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
