class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #DEFAULT VALUE IS 0, SO DON'T HAVE TO WORRY ABOUT HANDLING
        stack = [] #pair: [temp,index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([temp,i])
        return res





        