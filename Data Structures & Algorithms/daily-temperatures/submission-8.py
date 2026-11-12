class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures[i] represents daily temperatures on the ith day
        # return array res -> res[i] = number of days after ith day before a warmer temperature appears on a future day
        # none exist -> result[i] = 0


        # pattern: monotonic stack!
        # non-increasing 

        # 1. create res array (default 0), create stack
        # 2. iterate through temperatures
        # 3. find higher temperature than top of stack -> pop and compute difference
        # 4. Update res

        # temperatures = [30,38,30,36,35,40,28]
        # res = [1, 4, 1, 2, 1, 0, 0]
        # stack = [40, 28] 

        # TC: O(n)
        # SC: O(n)


        res = [0] * len(temperatures)
        stack = [] # [temp, i]

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                t, idx = stack.pop()
                res[idx] = i - idx

            
            stack.append([temp, i])
        
        return res
            






     


       





