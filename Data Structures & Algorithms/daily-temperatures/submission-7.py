class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures[i] represents daily temperatures on ith day
        # return array res, where res[i] is number of days after ith day before a warmer temperature appears 

        # Monotonic stack!
        # non-increasing

        # scan, find higher temperature than one at top of stack -> discovered "next warmer day" for earlier day

        # as we scan forward, whenever we find a temperature higher than the one on the top of the stack, it means we just discovered the "next warmer day" for that earlier day. 

        # pop -> compute difference in days -> continue


        # temperatures = [30,38,30,36,35,40,28]
        # res = [1, 4, 1, 2, 1, 0, 0]
        # stack = [40, 28] 

        stack = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            
            stack.append([t, i])
        
        return res


       





