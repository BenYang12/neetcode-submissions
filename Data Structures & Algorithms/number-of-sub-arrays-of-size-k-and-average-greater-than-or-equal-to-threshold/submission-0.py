class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #sliding window fixed size
        #return number of sub-arrays of size k and average >= threshold
        L = 0
        tot = 0
        res = 0
        for R in range(len(arr)):
            tot+=arr[R]

            if (R - L) + 1 == k:
                if tot / k >= threshold:
                    res += 1
                tot -= arr[L]
                L += 1
        return res
            
            
            
           
        return res

            

       
        