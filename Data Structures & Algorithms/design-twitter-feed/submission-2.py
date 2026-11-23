class Twitter:

        # follow/unfollow: hashMap, userId -> set of followeeId (constant time insert and remove)
        # postTweet: hashMap, userId -> list of [count, tweetId] (constant time add)

        # getNewsFeed: 
        # start by pushing latest tweet from each followee
        # smaller count means tweet is more recent
        # when we pop a tweet, push the next older tweet from that same user
        # repeat this until we collect 10 tweets
        # one user can still contribute many tweets if they are the most recent

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId
        
    


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # make sure each user follows themselves
        self.followMap[userId].add(userId)

        # for each followee:
        # 1. push their most recent tweet into a min-heap...
        # [time, tweetId, followeeId, nextIndex]
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        
        # while heap is not empty and result has < 10 tweets:
        # 1. pop most recent tweet
        # 2. add tweetId to result
        # 3. if followee has older tweets, push the next one into the heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)


            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
           
        # return collected tweets
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
