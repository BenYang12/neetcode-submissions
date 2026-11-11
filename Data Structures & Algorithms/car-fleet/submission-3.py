class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position[i] = position of ith car
        # speed[i] = speed of ith car
        # destination is at position target miles


        # target = 10, position = [1, 4], speed = [3, 2]
        # [[1, 3], [4, 2]], target = 10
        # time to reach target = 3, 3
        # thus, they meet each other at 10, the destination
        # return 1

        # use stack helps us easily compare each car's time with the fleet ahead of it

        # [3, 3]


        # cars that start closer to the target are processed first (sort by position)
        # for each car, compute TIME it takes to reach the target
        # push this time on to a stack
        # if new car's time is less than or equal to time before it, it catches up and merges with that fleet -> pop from stack
        # If car behind reaches target no faster than car in front -> catch up and join same fleet
        # number of remaining times in the stack equals the number of fleets -> return stack size
        # monotonic increasing stack

        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort(reverse = True)

        stack = [] # populate with time to reach destination

        for p, s in pairs:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            
           

     



       



            

        