class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] = number of bananas in ith pile, h = hours
        # decide k = bananas-per-hour
        # return min integer k s.t. all bananas can be eaten within h hours


        # Input: piles = [1,4,3,2], h = 9
        # Output = 2
        # 1 + 2 + 2 + 1 < 9

        # min eating speed k = 1
        # max eating speed k = max(piles) = 4
        # binary search over [1, 4]




        # Binary search interval -> [1, 4]
        low = 1
        high = max(piles)

        
        res = float("inf")
        while low <= high:
            speed = (low + high) // 2 # candidate eating speed

            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)

            
            if time <= h:
                # time is fast enough -> try to reduce more (go left)
                high = speed - 1
                res = min(res, speed)
            
            else:
                # current speed is too slow -> increase
                low = speed + 1
        return res
                




            
           








        

       