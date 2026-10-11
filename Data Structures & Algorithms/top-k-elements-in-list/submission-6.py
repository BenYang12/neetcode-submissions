class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums, k -> return k most frequent elements within array
        # need to know how often each number appears
        # after counting frequencies -> sort unique numbers
        # after sorting, highest frequencies appear at end
        # take the last k entries to get k most frequent elements
        

        #count frequencies -> sort by frequency -> take top k

        count = {} # create hashmap

        for num in nums:
            count[num] = 1 + count.get(num, 0) # {7 : 2, ...}
        
        # sort by value
        # {2 : 7, ...}
        # count: num
        arr = []
        for key, val in count.items():
            arr.append([val, key])
        arr.sort()


        # return k most frequent
        # [1, 2, 3]
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res





        
        
        


        






            
        


        