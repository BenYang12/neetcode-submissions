class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        #sort list of pairs
        #i stands for interval
        intervals.sort(key = lambda i: i[0]) #for each element i in data, compute key as i[0]
        output = [intervals[0]]

        for start,end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                #overlapping -> merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])
            
        return output


        