class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #num:frequency

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        reversed = []
        for num, cnt in count.items():
            reversed.append([cnt, num]) #frequency: num
        reversed.sort() #sort by frequency in ascending order

        output = []
        while len(output) < k:
            output.append(reversed.pop()[1])
        return output



        