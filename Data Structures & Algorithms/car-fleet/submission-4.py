class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars traveling to same destination
        # position[i] = position of ith car (miles)
        # speed[i] = speed of ith car (mph)
        # destination is at point target miles

        # car can't pass another car ahead of it, can only catch up and merge
        # care fleet = set of cars driving at same position + speed (single car)

        # return number of different car fleets

        # target = 10, position = [1, 4], speed = [3, 2]
        # output = 1



        # ALG:
        # sort by position (descending)
        # iterate from largest to smallest position
        # calculate time to target 
        # if time <= time at top of the stack -> car "behind" arrives "faster" -> merge
        # aka pop from stack -> keep slower car at the top of the stack
        # monotonic increasing stack
        # return len of stack

        # TC: O(nlogn)
        # SC: O(n)


        pairs = [[position, speed] for position, speed in zip(position, speed)]
        pairs.sort(reverse = True)
        
        stack = [] # monotonic increasing

        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)









     



     

        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort(reverse = True)

        stack = [] # populate with time to reach destination

        for p, s in pairs:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            
           

     



       



            

        