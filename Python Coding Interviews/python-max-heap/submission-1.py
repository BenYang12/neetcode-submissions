import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    #list of integers -> reverse sorted order
    #list of integers given is not necessarily a heap
    res = []

    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
    
    while max_heap:
        res.append(-heapq.heappop(max_heap))
    return res





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
