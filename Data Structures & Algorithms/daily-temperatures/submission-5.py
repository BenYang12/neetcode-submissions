class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[i, tmp]

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][1]:
                popped_ind, popped_tmp = stack.pop()
                res[popped_ind] = i - popped_ind
            stack.append([i,tmp])
        return res


   






         