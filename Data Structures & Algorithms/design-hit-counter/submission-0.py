# naive way storing all time stamps wastes memory and requires scanning entire history on each query


# key insight -> only need hits from past 300 seconds -> use queue to maintain sliding window

class HitCounter:

    def __init__(self):
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            diff = timestamp - self.hits[0]
            if diff >= 300:
                self.hits.popleft()
            else:
                break
        return len(self.hits)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
