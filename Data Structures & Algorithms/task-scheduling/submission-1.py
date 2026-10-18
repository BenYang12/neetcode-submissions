class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks[i] -> A-Z
        # integer n

        # Each CPU cycle allows completion of single task
        # Identical tasks must be separated by at least n CPU cycles
        # return minimum number of CPU cycles required to complete all tasks


        # Key to problem: process more frequent character first! Each task takes 1 unit time, minimize idle time
        # keep max-heap of tasks by their remaining count (most frequent on top)
        # at each unit of time, take most frequent available task and run it
        # after running a task, it goes into a cooldown queue with time current time + n
        # When a task's cooldown finishes, we push it back into the heap, so it can be scheduled again. 
        # if the heap is empty, but some tasks are still in cooldown, we can jump the current time forward to next time when a task becomes avaialble. 

        count = Counter(tasks) #{A: 3}
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap) # each entry is "remaining count" of a task 

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
                




       












        time = 0
        q = deque() #[-cnt, idleTime] #cooldown queue

        #process while maxHeap is non-empty or q is non-empty
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n ])
                
            if q and q[0][1] == time:
                #we can pop from q
                heapq.heappush(maxHeap,q.popleft()[0])
        
        return time
                





  
        