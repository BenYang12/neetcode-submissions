# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


#insertion sort is stable -> relative order will be maintained by default

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = [] #intermediate states

        for i in range(len(pairs)):  #cannot use i
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j] #swapping
                j -= 1

            res.append(pairs[:])#object, so clone it 
        return res


        