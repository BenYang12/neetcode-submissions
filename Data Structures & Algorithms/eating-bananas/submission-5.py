class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # banana-per-hour eating speed k
        # return minimum integer k s.t. koko can eat all the bananas within h hours

        # Input: piles = [3,6,7,11], h = 8
        # Output: 4
        # 1 + 2 + 2 + 3 = 8

        # k = [1, max[piles]]
        # run a binary search on this range
        # TC: O(logn)
        # SC: O(1)

        low = 1
        high = max(piles)
        res = float("inf")
        # 1 - 11

        while low <= high:
            k = (low + high) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            
            if time <= h:
                # eating speed is fast enough, try to find a slower eating speed
                res = min(res, k)
                high = k - 1
            else:
                # eating speed isn't fast enough, so I need to increase it
                low = k + 1
        
        return res
        

            




        

        
        
        