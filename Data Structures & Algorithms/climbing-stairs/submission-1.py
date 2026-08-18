class Solution:
    def climbStairs(self, n: int) -> int:
        # integer n = number of steps to reach the top of a staircase 
        # climb with either 1 or 2 steps at a time

        #Bottom Up DP!
        # to reach step i, I can only come from step i - 1 or step i - 2.
        # so, the total ways to reach step i is the sum of ways to reach 
        # the previous two steps -> Fibonacci

        if n <= 2:
            return n

        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one





        