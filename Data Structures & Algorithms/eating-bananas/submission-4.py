class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # instead of checking every speed, just check [1, max(piles)]

        low = 1
        high = max(piles)
        res = float("inf")

        while low <= high:
            k = (low + high) // 2
            
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            

            if totalTime <= h:
                # k works -> try to find smaller!
                high = k - 1
                res = min(res, k)
            
            else:
                # k is too small -> try to find bigger!
                low = k + 1
        return res
        


            



        