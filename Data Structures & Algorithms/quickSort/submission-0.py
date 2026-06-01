# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        #in place sorting algorithm
        self.quickSortHelper(pairs,0 ,len(pairs)-1)
        return pairs
        
    def quickSortHelper(self, pairs, s: int, e: int):
        #base case
        if e - s + 1 <= 1:
            return pairs #not neccesary to return 
            
        pivot = pairs[e] #Right most
        left = s

        for i in range(s,e):
            #Partition
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1

        #swap pivot with elem at left pivot
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, s, left-1)#left
        self.quickSortHelper(pairs, left+1, e)#right
            
            
                    

            

            


        