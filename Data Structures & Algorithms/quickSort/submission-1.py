# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs,0,len(pairs)-1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair],s, e):
        #base case
        if e - s + 1 <= 1:
            return pairs
        #Once we pick a pivot we will partition the array such that all elements less than or equal to the pivot are on the left and the rest are on the right.
        #We will then recursively run quicksort on the left and right halves until we hit the base case which is an array of size 1.
        pivot = pairs[e]#pivot is last elem
        left = s#pointer for left side

        #partition: elements smaller than pivot on left side
        for i in range(s,e):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1
        pairs[e] = pairs[left]
        pairs[left] = pivot

        #recursive calls, quick sort left side
        self.quickSortHelper(pairs,s, left-1)
        self.quickSortHelper(pairs, left+1,e)







        