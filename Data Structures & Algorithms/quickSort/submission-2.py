# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) -1)
        return pairs
        

    def quickSortHelper(self, arr:List[Pair], s:int, e:int) -> None:

        #base case
        if e - s + 1 <=1:
            return arr

        pivot = arr[e] #pivot is last element
        left = s #pointer for  left side

        #partition
        for i in range(s,e):
            if arr[i].key < pivot.key: #swap with left
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left+=1
        
        #swap left pointer with pivot to make sure pivot is between left and right sides
        arr[e] = arr[left]
        arr[left] = pivot


        #quick sort left side
        self.quickSortHelper(arr,s,left-1)
        self.quickSortHelper(arr, left + 1, e)
        

        