# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs: List[Pair], s , e):
        #base case
        if e - s + 1 <= 1:
            return pairs

        #calculate middle index
        m = (s + e) // 2

        #sort left
        self.mergeSortHelper(pairs, s, m)
        
        #sort right
        self.mergeSortHelper(pairs, m+1, e)

        #merge sorted halfs
        self.merge(pairs,s,m,e)

        return pairs

    def merge(self, arr, s, m, e):
        #Copy sorted left and right halfs to temp arrays
        L = arr[s:m+1]
        R = arr[m+1: e+1]

        i = 0 #index for left
        j = 0 # index for right
        k = s #index for arr

        #Merge two sorted halfs into original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        #One halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

