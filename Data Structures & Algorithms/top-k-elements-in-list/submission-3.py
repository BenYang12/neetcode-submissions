class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Sorting Solution
        res = []


        #nums, k -> return k most frequent elements within array
        #hashmap: {num: occurrences}
        #hashmap -> list of pairs (reverse order) -> [(4,1), ]
        #sort, then pop k times

        count = {} #num: occurrences

        for n in nums:
            count[n] = 1 + count.get(n,0)

        #{1:1, 2:2, 3:3}

        arr = []
        for key, value in count.items():
            arr.append([value, key])
        arr.sort()

        #[[1,1], [2,2], [3,3]]
        for i in range(k):
            res.append(arr.pop()[1])

        return res


        


        