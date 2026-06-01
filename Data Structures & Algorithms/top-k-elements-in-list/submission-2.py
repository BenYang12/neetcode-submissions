class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dict to keep track of frequency of each elem -> elem: # of occurrences
        #sort dict by values, to do this, append key value pairs into a list in reversed order, then sort that list (default in ascending order)
        #since values with highest will be towards the end, pop until we have k elements in res

        count = {} #num: count of nums
        for num in nums:
            count[num] = 1 + count.get(num,0) #{1: 13}

        
        sortarr = []
        for num, cnt in count.items():
            sortarr.append([cnt, num])
        sortarr.sort() #[13:1]

        res = []
        while len(res) < k:
            res.append(sortarr.pop()[1])
        
        return res

        #TC: O(nlogn)
        #SC: O(n)


        


            


