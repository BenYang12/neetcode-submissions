class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #arr, k, threshold -> number of sub-arrays of size k and average >= threshold
        L = 0
        curSum = 0
        res = 0

        for R in range(len(arr)):

            curSum += arr[R] #PUT THIS BEFORE THE CHECK
            
            if R - L + 1 == k:
                if curSum / k >= threshold:
                    res += 1
                curSum -= arr[L]
                L += 1
            
            
            
        
        return res
            





        