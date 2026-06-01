# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, s, e) -> None:
        #base case
        if e - s + 1 <= 1:
            return pairs

        pivot = pairs[e] #pivot is last element
        l = s #pointer for left side


        #partition: elements smaller than pivot on left side
        for i in range (s, e):
            if pairs[i].key < pivot.key:
                #swap with left
                tmp = pairs[i]
                pairs[i] = pairs[l]
                pairs[l] = tmp
                l+=1
        #final swap
        # Move pivot in-between left & right sides
        pairs[e] = pairs[l]
        pairs[l] = pivot

        self.quickSortHelper(pairs, s, l-1)
        self.quickSortHelper(pairs,l+1,e)

        


        







        