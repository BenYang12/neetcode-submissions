class Solution:
    def reorganizeString(self, s: str) -> str:
        # maxHeap efficiently gives us most frequent char at any time

        # pop top character, add it to res, then push back w/ decremented count after 
        # processing the next character
        # delay ensures we never place the same character twice in a row

        # if heap is empty, but we still have a prev pending character:
        # reorganization failed

        count = {} # char: freq of char
        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # O(n)


        prev = None
        res = ""
        while maxHeap or prev:
            # keep loopinga s long as there's either a character in the heap
            # to place OR a character being held in prev
            if prev and not maxHeap:
                # if we're holding a character in prev BUT the heap is now 
                # empty, its impossible. We can't place that held character
                # without repeating it, return ""
                return ""
            

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        return res