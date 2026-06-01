class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #pattern: monotonic stack
        #iterate through temperatures, storing both index and temperature
        #if I run into a tmp that is > tmp at top of stack, I pop the stack tmp, and at its index in output I store the difference in index
        

        #res initialized to 0 at first, as I'm told to set result[i] to 0 if there is no day in the future where a warmer temperature will appear
        res = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):

            while stack and tmp > stack[-1][0]:
                stackTmp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            
            stack.append([tmp,i])
        return res



        
        