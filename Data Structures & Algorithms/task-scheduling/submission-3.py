class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Input: tasks = ["X","X","Y","Y"], n = 2
        # Output: 5, X-> Y -> idle -> X -> Y

        # always run task that has most remaining occurrences
        # those tasks are hardest to fit into schedule

        # keep max-heap of tasks by their remaining count
        # after running task, add to a cooldown queue w/ time its available again
        # when a task's cooldown finishes, push it back into the heap for rescheduling
        # heap empty, some tasks in cooldown -> jump current time forward


        # hashmap 
        count = {} # task: freq
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        

        # build a max heap, where each entry is "remaining count" of a task
        # only add counts of tasks (integer) to heap, not tasks
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap) # O(n)


        time = 0
        q = deque() # pairs of [ -cnt, next_available_time]
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    q.append([cnt, time + n])
            
            while q and q[0][1] == time:
                cnt = q.popleft()[0]
                if cnt < 0:
                    heapq.heappush(maxHeap, cnt)
        return time
            


            
                














        
        