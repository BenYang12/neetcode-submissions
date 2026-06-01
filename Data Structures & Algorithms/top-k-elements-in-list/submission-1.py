class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} #num: count of nums
        output = []

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        #I now have a hashmap -> num: count of nums
        #I need to sort by count of nums

        reversed_list = []
        for key,value in hashMap.items():
            reversed_list.append([value,key])
        #I now have a list of key value pairs where key is the count of nums, I can sort by key in place
        #.sort() sorts in ascending order, highest values at end, so I need to pop
        reversed_list = sorted(reversed_list)

        while len(output) < k:
            output.append(reversed_list.pop()[1])
        return output




        