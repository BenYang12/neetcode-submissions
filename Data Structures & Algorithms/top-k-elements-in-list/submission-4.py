class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #num: number of occurrences for num
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        new_list = []
        for key, value in count.items():
            new_list.append([value, key])
        
        new_list.sort()

        res=[]

        for i in range(k):
            res.append(new_list.pop()[-1])
        
        return res
           
            
        

        